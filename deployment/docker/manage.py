#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Make sure manage.py can be called from the $PATH
    from django.core.management import execute_from_command_line
    os.chdir('/app/src')
    sys.path.insert(0, '/app/src')
    execute_from_command_line(sys.argv)
