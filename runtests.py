#!/usr/bin/env python
import sys
import os
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.unittest")

    TEST_APPS = [
        '{{ project_name }}',  # also takes subfolders
        'frontend',
    ]

    argv = sys.argv[:1] + ['test', '--traceback'] + (sys.argv[1:] or TEST_APPS)
    execute_from_command_line(argv)
