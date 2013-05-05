"""
Project specific settings
"""
from .defaults import *

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('{{ project_name }}', 'sysadmin@edoburu.nl'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'sysadmin@edoburu.nl'
EMAIL_SUBJECT_PREFIX = '[Django][{{ project_name }}] '

# Database to use
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     '{{ project_name }}',
        'USER':     '{{ project_name }}',
        'PASSWORD': '',
    },
}

SECRET_KEY = '{{ secret_key }}'

# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',

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
    'django_wysiwyg',
    'django.contrib.comments',
    'filebrowser',
    'google_analytics',
    'mptt',
    'polymorphic',
    'polymorphic_tree',
    'taggit',
    'taggit_autocomplete_modified',
    'sorl.thumbnail',
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

# App specific settings
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'

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

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache',)  # sorl.thumbnail generated files
FILEBROWSER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # in bytes
