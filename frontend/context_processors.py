from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject


def frontend(request):
    """
    Additional variables to include in *every* template.
    """
    site = SimpleLazyObject(lambda: get_current_site(request))
    http_scheme = 'https://' if request.is_secure() else 'http://'

    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "{0}{1}".format(http_scheme, site.domain)),
    }
