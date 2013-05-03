from django.core.wsgi import get_wsgi_application
from . import bootstrap_wsgi_settings

# Add the project to sys.path,
# set DJANGO_SETTINGS_MODULE to PROJECT_NAME.settings.env.THIS_FILENAME
bootstrap_wsgi_settings(__file__)

# Export application object
application = get_wsgi_application()
