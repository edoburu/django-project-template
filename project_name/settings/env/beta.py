from .. import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
