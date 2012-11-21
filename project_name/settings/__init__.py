# This is what manage.py and friends read.
from .project import *

# Easily allow local settings
try:
    from .local import *
except ImportError:
    pass
