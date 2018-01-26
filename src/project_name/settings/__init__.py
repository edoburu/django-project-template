# This is what manage.py and friends read.
import sys
from .defaults import *


if sys.version_info[0:2] < (3, 6):
    ModuleNotFoundError = ImportError

# Easily allow local settings
try:
    from .local import *
except ModuleNotFoundError:
    pass
