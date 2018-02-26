# Build environment has gcc and develop header files.
# The installed files are copied to the smaller runtime container.
FROM edoburu/django-base-images:py36-stretch-build AS build-image

# Install (and compile) all dependencies
RUN mkdir -p /app/src/requirements
COPY src/requirements/*.txt /app/src/requirements/
ARG PIP_REQUIREMENTS=/app/src/requirements/docker.txt
RUN pip install --no-binary=Pillow -r $PIP_REQUIREMENTS

# Remove unneeded files
RUN find /usr/local/lib/python3.6/site-packages/ -name '*.po' -delete

# Node builder
FROM node:9-stretch as frontend-build
RUN mkdir -p /app/src
WORKDIR /app/src
COPY src/package.json src/package-lock.json* /app/src/
RUN npm install
COPY src/gulpfile.js /app/src/
COPY src/frontend/ /app/src/frontend/
RUN npm run gulp

# Start runtime container
FROM edoburu/django-base-images:py36-stretch-runtime
ENV UWSGI_PROCESSES=1 \
    UWSGI_THREADS=10 \
    UWSGI_OFFLOAD_THREADS=5 \
    UWSGI_MODULE={{ project_name }}.wsgi.docker:application \
    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.docker

# System config (done early, avoid running on every code change)
MAINTAINER vdboor@edoburu.nl
EXPOSE 8080 1717
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:8080/api/health/ || exit 1

# Install dependencies
COPY --from=build-image /usr/local/bin/ /usr/local/bin/
COPY --from=build-image /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/
COPY --from=frontend-build /app/src/frontend/static /app/src/frontend/static

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
    #whitenoise does this;
    #gzip --keep --best --force --recursive /app/web/static/ && \
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
