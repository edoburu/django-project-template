from .. import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     '{{ project_name }}',
        'USER':     '{{ project_name }}',
        'PASSWORD': '',
    },
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

ALLOWED_HOSTS = (
    '{{ project_name }}.testing.mycompany.tld',
)

CACHES['default']['KEY_PREFIX'] = '{{ product_name }}.beta'

#INSTALLED_APPS += ('gunicorn',)
