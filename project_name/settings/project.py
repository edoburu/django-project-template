"""
Project specific settings
"""
from .defaults import *

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
    'apps.wysiwyg_config',

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

    # Support libs
    'any_imagefield',
    'any_urlfield',
    'categories',
    'categories.editor',
    'crispy_forms',
    'django.contrib.comments',
    'django_wysiwyg',
    'filebrowser',
    'google_analytics',
    'mptt',
    'polymorphic',
    'polymorphic_tree',
    'sorl.thumbnail',
    'taggit',
    'taggit_autocomplete_modified',
    'tinymce',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'frontend.context_processors.site',
)

FORMAT_MODULE_PATH = '{{ project_name }}.settings.locale'  # Consistent date formatting

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s: %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'simple': {
            'format': '%(levelname)s: %(message)s',
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
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['console'],
            'level': 'ERROR',  # to show queries or not.
        },
    }
}


## -- Third party app settings

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

COMMENTS_APP = 'fluent_comments'

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache',)  # sorl.thumbnail generated files
FILEBROWSER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # in bytes

FLUENT_BLOGS_BASE_TEMPLATE = 'base_blog.html'
FLUENT_BLOGS_ENTRY_LINK_STYLE = '/{year}/{month}/{slug}/'

FLUENT_CONTENTS_CACHE_OUTPUT = True

text_plugins = ('TextPlugin', 'PicturePlugin', 'OEmbedPlugin', 'SharedContentPlugin', 'RawHtmlPlugin',)
FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
    # This limits which plugins can be used for certain placeholder slots.
    'main': {
        'plugins': text_plugins
    },
}

FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(SRC_DIR, 'frontend', 'templates')
