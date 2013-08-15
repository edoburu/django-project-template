from .. import *
from os.path import dirname
import sys

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': dirname(dirname(dirname(__file__))) + '/testdatabase.db'
}

if sys.argv[1] in ['test']:
    print "Using in memory database.\n"
