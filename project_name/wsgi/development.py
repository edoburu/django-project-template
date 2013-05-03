"""
Development WSGI config for {{ project_name }} project.

This module contains the WSGI application used by Django's development server.
Django's ``runserver`` and ``runfcgi`` commands discover this application
via the ``WSGI_APPLICATION`` setting.

Each production site can use one of the other modules in this folder;
the production/beta WSGI files auto-detect their system paths and location.
"""
from django.core.wsgi import get_wsgi_application

# Export application object
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
