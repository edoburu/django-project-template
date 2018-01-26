from django.conf import settings


def git_version():
    return getattr(settings, 'GIT_VERSION', 'Unknown')
