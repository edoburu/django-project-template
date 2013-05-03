from os.path import dirname, basename, realpath
import os
import sys


def bootstrap_wsgi_settings(wsgi_file, env_name=None):
    """
    Setup the base configuration:

    * Includes the project root to ``sys.path``
    * Set ``DJANGO_SETTINGS_MODULE`` to ``PROJECT_NAME.settings.env.WSGI_FILENAME`` by default.

    This function assumes the ``wsgi_file`` is stored at: src_folder/project_name/settings/env/env_name.py
    """
    if not env_name:
        env_name = basename(wsgi_file).split('.')[0]

    wsgi_file = realpath(wsgi_file)
    project_folder = dirname(dirname(wsgi_file))
    src_folder = dirname(project_folder)
    project_name = basename(project_folder)

    # Set startup settings
    # Avoid having to do this in the application server
    if src_folder not in sys.path:
        sys.path.append(src_folder)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_name + '.settings.env.' + env_name)

    # Redirect print statements to apache log
    sys.stdout = sys.stderr
