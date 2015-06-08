"""
The default settings for any Django project.
Place project customizations in ``project.py``.
"""
import os, re

DEBUG          = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = ''


## --- Internal settings

SITE_ID = 1

# Language codes
USE_I18N = True                   # False for optimizations
USE_L10N = True
USE_TZ = True

# Path autodetection
SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
ROOT_DIR = SRC_DIR  # os.path.dirname(SRC_DIR)

# Paths
MEDIA_ROOT   = ROOT_DIR + '/web/media/'
MEDIA_URL    = '/media/'        # Must end with /
ROOT_URLCONF = '{{ project_name }}.urls'

STATIC_ROOT = ROOT_DIR + '/web/static/'
STATIC_URL  = '/static/'

SESSION_COOKIE_HTTPONLY = True  # can't read cookie from JavaScript
X_FRAME_OPTIONS = 'SAMEORIGIN'  # Prevent iframes. Can be overwritten per view using the @xframe_options_.. decorators

INTERNAL_IPS = ('127.0.0.1',)

IGNORABLE_404_URLS = (
    re.compile(r'^favicon.ico$'),
)


## --- Plugin components

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'compressor',
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

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


## --- App settings

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_ENABLED = False
