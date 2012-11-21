from .. import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

CACHES = {
     'default': {
         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
         'KEY_PREFIX': '{{ project_name }}.prd',
         'LOCATION': '127.0.0.1:11211',
         'TIMEOUT': 24*3600
     },
}
