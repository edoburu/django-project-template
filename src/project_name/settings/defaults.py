"""
The settings for this project.
"""
import logging
import os

import environ
import raven.exceptions

env = environ.Env()

## --- Environment

SITE_ID = 1
DEBUG = env.bool('DJANGO_DEBUG', True)

SRC_DIR = str(environ.Path(__file__) - 3)
ROOT_DIR = str(environ.Path(__file__) - 4)

# Paths
MEDIA_ROOT = ROOT_DIR + '/web/media/'
MEDIA_URL = '/media/'        # Must end with /
ROOT_URLCONF = '{{ project_name }}.urls'

STATIC_ROOT = ROOT_DIR + '/web/static/'
STATIC_URL = '/static/'

# --- Locale settings

LANGUAGE_CODE = 'nl'
TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True                   # False for optimizations
USE_L10N = True
USE_TZ = True

# --- Email

# -------------------------------------
# TODO: update the email settings here!
# -------------------------------------

ADMINS = (
    ('{{ project_name }}', 'sysadmin@{{ project_name }}.example.org'),
)
MANAGERS = (
    ('Website {{ project_name }}', 'info@{{ project_name }}.example.org'),
)

SERVER_EMAIL = 'root@localhost'
DEFAULT_FROM_EMAIL = 'info@{{ project_name }}.example.com'
EMAIL_SUBJECT_PREFIX = '[Django][{{ project_name }}] '


# --- Security

SECRET_KEY = env.str('DJANGO_SECRET_KEY', '{{ secret_key|safe }}')
SESSION_COOKIE_HTTPONLY = True  # can't read cookie from JavaScript
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', not DEBUG)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', not DEBUG)

X_FRAME_OPTIONS = 'DENY'  # Prevent iframes. Can be overwritten per view using the @xframe_options_.. decorators

INTERNAL_IPS = ('127.0.0.1',)

IGNORABLE_404_URLS = (
    # re.compile(r'^/favicon.ico$'),
    # re.compile(r'^/wp-login.php$'),
)

# --- Plugin components

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'compressor',

    # Site parts
    'frontend',
    '{{ project_name }}.apps.wysiwyg_config',

    # CMS parts
    'fluent_blogs',
    'fluent_blogs.pagetypes.blogpage',
    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',
    'fluent_pages.pagetypes.redirectnode',
    'fluent_comments',
    'fluent_contents',
    'fluent_contents.plugins.text',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.rawhtml',
    'fluentcms_button',
    'fluentcms_contactform',
    'fluentcms_jumbotron',
    'fluentcms_pager',
    'fluentcms_teaser',

    # Support libs
    'analytical',
    'any_imagefield',
    'any_urlfield',
    'axes',
    'categories_i18n',
    'crispy_forms',
    'django_comments',
    'django_wysiwyg',
    'filebrowser',
    'mptt',
    'parler',
    'polymorphic',
    'polymorphic_tree',
    'slug_preview',
    'sorl.thumbnail',
    'staff_toolbar',
    'taggit',
    'taggit_autosuggest',
    'tinymce',
    'webmaster_verification',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

FORMAT_MODULE_PATH = '{{ project_name }}.settings.locale'  # Consistent date formatting

LOCALE_PATHS = (
    os.path.join(SRC_DIR, 'locale'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Generate cache-busing static file names that can have a far-future expire headers
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = (
    'raven.contrib.django.middleware.SentryLogMiddleware',       # make 'request' available on all logs.
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',  # on 404, report to sentry.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fluent_contents.middleware.HttpRedirectRequestMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (),
        'OPTIONS': {
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader',  # Allow {% extends "appname:template" %}
            ),
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'frontend.context_processors.frontend',
            ),
        },
    },
]

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# --- Services

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

CACHES = {
    'default': env.cache(default='redis://localhost:6379/1?KEY_PREFIX=={{ project_name }}'),
}

DATABASES = {
    'default': env.db(default='postgresql://{{ project_name }}:testtest@localhost/{{ project_name }}'),
}

locals().update(env.email_url(default='smtp://'))

RAVEN_CONFIG = {
    'dsn': env.str('SENTRY_DSN', default=''),
}

try:
    GIT_VERSION = raven.fetch_git_sha('..')
    RAVEN_CONFIG['release'] = GIT_VERSION
except raven.exceptions.InvalidGitRepository:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': u'%(levelname)s: %(asctime)s %(process)d %(thread)d %(module)s: %(message)s',
        },
        'simple': {
            'format': u'%(levelname)s:\t%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': 'ERROR',  # to show queries or not.
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}


# -- Third party app settings

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

AXES_LOGIN_FAILURE_LIMIT = 6
AXES_COOLOFF_TIME = 1  # hours
AXES_IP_WHITELIST = INTERNAL_IPS

CRISPY_TEMPLATE_PACK = 'bootstrap3'

COMMENTS_APP = 'fluent_comments'

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', not DEBUG)

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'

FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

FILE_UPLOAD_PERMISSIONS = 0o644  # Avoid 600 permission for filebrowser uploads.

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache', '_versions', '_admin_thumbnail\.', '_big\.', '_large\.', '_medium\.', '_small\.', '_thumbnail\.')
FILEBROWSER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # in bytes
FILEBROWSER_STRICT_PIL = True
FILEBROWSER_ADMIN_VERSIONS = [
    'thumbnail',
    #'small',
    #'medium',
    #'big',
    #'large',
]
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large', 'width': 680, 'height': '', 'opts': ''},
}
FILEBROWSER_VERSION_QUALITY = 80  # Good enough visually, and for Google Pagespeed

FLUENT_BLOGS_BASE_TEMPLATE = 'base_blog.html'
FLUENT_BLOGS_ENTRY_LINK_STYLE = '/{year}/{month}/{slug}/'

FLUENT_CONTENTS_CACHE_OUTPUT = True

text_plugins = ('TextPlugin', 'PicturePlugin', 'OEmbedPlugin', 'RawHtmlPlugin',)
FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
    # This limits which plugins can be used for certain placeholder slots.
    'homepage': {
        'plugins': text_plugins + ('SharedContentPlugin', )
    },
    'main': {
        'plugins': text_plugins + ('SharedContentPlugin', )
    },
    'shared_content': {
        'plugins': text_plugins,
    }
}

FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(SRC_DIR, 'frontend', 'templates')

FLUENT_TEXT_CLEAN_HTML = True
FLUENT_TEXT_SANITIZE_HTML = True
FLUENT_TEXT_PRE_FILTERS = (
    'fluent_contents.plugins.text.filters.smartypants.smartypants_filter',
)

GOOGLE_ANALYTICS_PROPERTY_ID = env.str('GOOGLE_ANALYTICS_PROPERTY_ID', None)

HEALTH_CHECKS = {
    'database': 'django_healthchecks.contrib.check_database',
    'cache': 'django_healthchecks.contrib.check_cache_default',
    'ip': 'django_healthchecks.contrib.check_remote_addr',
    'git_version': '{{ project_name }}.lib.healthchecks.git_version',
}
HEALTH_CHECKS_ERROR_CODE = 503

IPWARE_META_PRECEDENCE_ORDER = (
    # Avoid IP address spoofing for django-axes. Use wsgi-unproxy instead,
    # which tests against a fixed set of incoming sender addresses.
    'REMOTE_ADDR',
)

TAGGIT_CASE_INSENSITIVE = True

THUMBNAIL_DEBUG = True
THUMBNAIL_FORMAT = 'JPEG'
THUMBNAIL_QUALITY = 80  # default quality for mozjpeg's "cjpeg -optimize" is 75
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2]  # Generate 2x images for everything!

WEBMASTER_VERIFICATION = env.dict('WEBMASTER_VERIFICATION', default={})

if not DEBUG:
    # Production specific settings.
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )

    # Uncomment in case the site runs behind an HTTP proxy (e.g. Gunicorn)
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    TEMPLATES[0]['OPTIONS']['loaders'] = (
        ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
    )
