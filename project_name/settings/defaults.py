# Django settings for edoburu project.
import os, re

DEBUG          = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = ''

# People who receive 500 errors
ADMINS = (
    ('{{ project_name }}', 'sysadmin@edoburu.nl'),
)

DEFAULT_FROM_EMAIL = 'sysadmin@edoburu.nl'

# People who receive 404 errors
MANAGERS = ADMINS


## --- Internal settings

SITE_ID = 1

# Language codes
USE_I18N = True                   # False for optimizations
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'nl_NL'

# Path autodetection
PROJECT_DIR  = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Paths
MEDIA_ROOT   = PROJECT_DIR + '/web/media/'
MEDIA_URL    = '/media/'        # Must end with /
ROOT_URLCONF = '{{ project_name }}.urls'

STATIC_ROOT = PROJECT_DIR + '/web/static/'
STATIC_URL  = '/static/'

SESSION_COOKIE_HTTPONLY = True  # can't read cookie from JavaScript
X_FRAME_OPTIONS = 'DENY'        # Prevent iframes. Can be overwritten per view using the @xframe_options_.. decorators

INTERNAL_IPS = ('127.0.0.1',)

IGNORABLE_404_URLS = (
    re.compile(r'^favicon.ico$'),
)


## --- Plugin components

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'compressor',
    'south',
)

TEMPLATE_DIRS = (
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'KEY_PREFIX': '{{ project_name }}.local',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 24*3600
    },
}


## --- App settings

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_ENABLED = False
