from .. import *
from os.path import dirname
import sys

if 'runtests.py' in sys.argv[0] or 'test' in sys.argv:
    print "Using in memory database.\n"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Avoid sending real emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
