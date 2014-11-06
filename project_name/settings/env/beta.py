from .. import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        #'ENGINE':   'django.db.backends.mysql',
        'NAME':     '{{ project_name }}',
        'USER':     '{{ project_name }}',
        'PASSWORD': '',
        'OPTIONS':  {'autocommit': True,},   # Stop that "current transaction is aborted" error in PostgreSQL
    },
}

INSTALLED_APPS += (
    #'gunicorn',
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

ALLOWED_HOSTS = (
    '{{ project_name }}.testing.mycompany.tld',
    '{{ project_name }}.testing.mycompany.tld.',
)

CACHES['default']['KEY_PREFIX'] = '{{ project_name }}.beta'
