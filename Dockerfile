# Build environment has gcc and develop header files.
# The installed files are copied to the smaller runtime container.
FROM python:3.6.4 as build-image
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

# Install all Pillow dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y libjpeg62-turbo-dev && \
    rm -rf /var/lib/apt/lists/* /var/cache/debconf/*-old

# Install (and compile) all dependencies
RUN mkdir -p /app/src/requirements
COPY src/requirements/*.txt /app/src/requirements/
ARG PIP_REQUIREMENTS=/app/src/requirements/unittest.txt
RUN pip install -r $PIP_REQUIREMENTS

# Remove unneeded files
RUN find /usr/local/lib/python2.7/site-packages/ -name '*.po' -delete

# Start runtime container
FROM python:3.6.4-slim
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    UWSGI_PROCESSES=1 \
    UWSGI_THREADS=10 \
    UWSGI_OFFLOAD_THREADS=5 \
    UWSGI_MODULE={{ project_name }}.wsgi.docker:application \
    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.docker

# Install runtime dependencies (can become separate base image)
# Also include gettext for now, so locale is still compiled here.
# It avoids busting the previous cache layers on code changes.
RUN apt-get update && \
    apt-get install --no-install-recommends -y libxml2 libjpeg62-turbo gettext mime-support && \
    rm -rf /var/lib/apt/lists/* /var/cache/debconf/*-old && \
    echo "font/woff2  woff2" >> /etc/mime.types && \
    useradd --system --user-group app

# System config (done early, avoid running on every code change)
MAINTAINER vdboor@edoburu.nl
EXPOSE 8080 1717
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:8080/api/ping/ || exit 1

# Install dependencies
COPY --from=build-image /usr/local/bin/ /usr/local/bin/
COPY --from=build-image /usr/local/lib/python2.7/site-packages/ /usr/local/lib/python2.7/site-packages/

# Insert application code.
# - Prepare gzipped versions of static files for uWSGI to use
# - Create a default database inside the container (as demo),
#   when caller doesn't define DATABASE_URL
# - Give full permissions, so Kubernetes can run the image as different user
ENV DATABASE_URL=sqlite:////tmp/demo.db
COPY web /app/web
COPY src /app/src
COPY deployment/docker/manage.py /usr/local/bin/
WORKDIR /app/src
RUN rm /app/src/*/settings/local.py* && \
    find . -name '*.pyc' -delete && \
    python -mcompileall -q */ && \
    manage.py compilemessages && \
    manage.py collectstatic --noinput --link && \
    manage.py migrate && \
    manage.py loaddata example_data.json && \
    #whitenoise does this; gzip --keep --best --force --recursive /app/web/static/ && \
    mkdir -p /app/web/media /app/web/static/CACHE && \
    chown -R app:app /app/web/media/ /app/web/static/CACHE /tmp/demo.db && \
    chmod -R go+rw /app/web/media/ /app/web/static/CACHE /tmp/demo.db

# Insert main code (still as root), then reduce permissions
# Allow to mount the compressor cache as volume too for sharing between pods.
COPY deployment/docker/uwsgi.ini /app/uwsgi.ini
CMD ["/usr/local/bin/uwsgi", "--ini", "/app/uwsgi.ini"]
VOLUME /app/web/media
VOLUME /app/web/static/CACHE

# Tag the docker image
ARG GIT_VERSION
LABEL git-version=$GIT_VERSION
RUN echo $GIT_VERSION > .docker-git-version

# Reduce default permissions
USER app
