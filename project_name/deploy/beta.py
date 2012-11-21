import os
import sys

# Detect current path;
# base_folder/module_name/settings/env/env_name.py
file_path = os.path.realpath(__file__)
env_name = os.path.basename(__file__).split('.')[0]
project_folder = os.path.dirname(os.path.dirname(file_path))
base_folder = os.path.dirname(project_folder)
module_name = os.path.basename(project_folder)

# Set startup settings
sys.path.append(base_folder)
os.environ['DJANGO_SETTINGS_MODULE'] = module_name + '.settings.env.' + env_name
sys.stdout = sys.stderr    # redirect print statements to apache log

# Export application object
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
