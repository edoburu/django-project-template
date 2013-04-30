import os
import sys

# Detect current path;
# src_folder/project_name/settings/env/env_name.py
file_path = os.path.realpath(__file__)
env_name = os.path.basename(__file__).split('.')[0]
project_folder = os.path.dirname(os.path.dirname(file_path))
src_folder = os.path.dirname(project_folder)
project_name = os.path.basename(project_folder)

# Set startup settings
# Avoid having to do this in the application server
sys.path.append(src_folder)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_name + '.settings.env.' + env_name)
sys.stdout = sys.stderr    # redirect print statements to apache log

# Export application object
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
