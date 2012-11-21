from settings.project import *
from os.path import dirname
import sys

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = dirname(dirname(dirname(__file__))) + '/testdatabase.db'

if sys.argv[1] in ['test']:
    print "Using in memory database.\n"
