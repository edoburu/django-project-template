import sys

from . import *

if 'runtests.py' in sys.argv[0] or 'test' in sys.argv:
    print("Using in memory database.\n")

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

#AXES_ENABLED = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    #'NAME': dirname(dirname(dirname(__file__))) + '/testdatabase.db'
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

COMPRESS_ENABLED = True

# Avoid sending real emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
