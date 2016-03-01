import admin_tools.urls
import django.contrib.sitemaps.views
import django.views.defaults
import django.views.static
import ping.urls

from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.utils.functional import curry
from filebrowser.sites import site as fb_site
from os import path
from frontend.views import TextFileView, Http500View

admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}

urlpatterns = [
    # Django admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(fb_site.urls)),
    url(r'^admin/util/tools/', include(admin_tools.urls)),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^400/$', curry(django.views.defaults.bad_request, exception=None)),
    url(r'^403/$', curry(django.views.defaults.permission_denied, exception=None)),
    url(r'^404/$', curry(django.views.defaults.page_not_found, exception=None)),
    url(r'^500/$', django.views.defaults.server_error),

    # SEO API's
    url(r'^sitemap.xml$', django.contrib.sitemaps.views.sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),

    # Monitoring API's
    url(r'^api/ping/', include(ping.urls)),

    # CMS modules
    # TODO: add your urls here
]

if settings.DEBUG:
    # For runserver, also host the media files
    # Sass files are exported so browsers can open the Sass sources via sourcemaps.
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^sass/(?P<path>.*)$', django.views.static.serve, {'document_root': path.join(settings.SRC_DIR, 'frontend', 'sass'), 'show_indexes': True}),
    ] + urlpatterns

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        # Debug toolbar is explicitly linked, no magic that breaks on first request errors.
        import debug_toolbar
        urlpatterns.insert(0,
            url(r'^__debug__/', include(debug_toolbar.urls))
        )
