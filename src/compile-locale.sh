#!/bin/sh
cd `dirname $0`
unset DJANGO_SETTINGS_MODULE

django-admin.py compilemessages
