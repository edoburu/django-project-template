from . import *

# Don't allow all hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['.{{ project_name }}.example.org'])

# Change some defaults
DEBUG = env.bool('DJANGO_DEBUG', default=False)
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', not DEBUG)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', not DEBUG)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', not DEBUG)

# Raven is only enabled in production to avoid warnings in development
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    #'gunicorn',
)

# Keep templates in memory
TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)
