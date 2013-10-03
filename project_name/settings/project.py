"""
Project specific settings
"""
from .defaults import *

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('{{ project_name }}', 'sysadmin@{{ project-name }}.example.org'),
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
    'crispy_forms',
    'filebrowser',
    'google_analytics',
    'sorl.thumbnail',

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

# App specific settings
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache',)  # sorl.thumbnail generated files
FILEBROWSER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # in bytes
