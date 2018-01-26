# This is what manage.py and friends read.
from .defaults import *

# Easily allow local settings
try:
    from .local import *
except ModuleNotFoundError:
    pass
