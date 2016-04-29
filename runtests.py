#!/usr/bin/env python
import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.env.unittest")

    TEST_APPS = [
        'apps',
        'frontend',
    ]

    argv = sys.argv[:1] + ['test', '--traceback'] + (sys.argv[1:] or TEST_APPS)
    execute_from_command_line(argv)
