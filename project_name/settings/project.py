"""
Project specific settings
"""
from .defaults import *

# -------------------------------------
# TODO: update the email settings here!
# -------------------------------------

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('{{ project_name }}', 'sysadmin@{{ project_name }}.example.org'),
)
MANAGERS = ADMINS

SERVER_EMAIL = 'root@localhost'
DEFAULT_FROM_EMAIL = 'info@{{ project_name }}.example.com'
EMAIL_SUBJECT_PREFIX = '[Django][{{ project_name }}] '

# Project language settings
TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'en'

# Database to use
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

SECRET_KEY = '{{ secret_key|safe }}'

# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',

    # Support libs
    'axes',
    'crispy_forms',
    'filebrowser',
    'googletools',
    'sorl.thumbnail',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.SentryLogMiddleware',       # make 'request' available on all logs.
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',  # on 404, report to sentry.
) + MIDDLEWARE_CLASSES + (
    'axes.middleware.FailedLoginMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'frontend.context_processors.frontend',
)

FORMAT_MODULE_PATH = '{{ project_name }}.settings.locale'  # Consistent date formatting

# Avoid 600 permission for filebrowser uploads.
FILE_UPLOAD_PERMISSIONS = 0644

IGNORABLE_404_URLS = (
    #re.compile(r'^/favicon.ico$'),
    #re.compile(r'^/wp-login.php$'),
)


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


## -- Third party app settings

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

AXES_LOGIN_FAILURE_LIMIT = 6
AXES_COOLOFF_TIME = 1  # hours
AXES_IP_WHITELIST = INTERNAL_IPS


FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache', '_admin_thumbnail\.', '_big\.', '_large\.', '_medium\.', '_small\.', '_thumbnail\.')
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

PING_CHECKS = (
    'ping.checks.check_database_sessions',
    'ping.checks.check_database_sites',
    #'ping.checks.check_celery', # Fails..
)
