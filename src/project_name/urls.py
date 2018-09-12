from os import path

import admin_tools.urls
import django.contrib.sitemaps.views
import django.views.defaults
import django.views.static
import django_healthchecks.urls
import webmaster_verification.urls
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from filebrowser.sites import site as fb_site

from frontend.views import Http500View, TextFileView, serve_web_file

sitemaps = {
    # Place sitemaps here
}

urlpatterns = [
    # Django admin
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', fb_site.urls),
    url(r'^admin/util/tools/', include(admin_tools.urls)),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^400/$', django.views.defaults.bad_request, kwargs={'exception': None}),
    url(r'^403/$', django.views.defaults.permission_denied, kwargs={'exception': None}),
    url(r'^404/$', django.views.defaults.page_not_found, kwargs={'exception': None}),
    url(r'^500/$', django.views.defaults.server_error),

    # SEO API's
    url(r'^sitemap.xml$', django.contrib.sitemaps.views.sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),
    url(r'', include(webmaster_verification.urls)),

    # Favicon (avoids nginx config)
    url(r'^(?P<path>(android-chrome|apple-touch|browserconfig|favicon|manifest|safari-pinned)[^/\.]*\.(json|png|ico|xml|svg))$',
        serve_web_file),

    # Monitoring API's
    url(r'^api/health/', include(django_healthchecks.urls)),

    # CMS modules
    # TODO: add your urls here
]

if settings.DEBUG:
    # For runserver, also host the media files
    # Sass files are exported so browsers can open the Sass sources via sourcemaps.
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^sass/(?P<path>.*)$', django.views.static.serve, {'document_root': path.join(settings.SRC_DIR, 'frontend/sass'), 'show_indexes': True}),
        url(r'^node_modules/bootstrap-sass/assets/(?P<path>.*)$', django.views.static.serve, {'document_root': path.join(settings.SRC_DIR, 'node_modules/bootstrap-sass/assets/'), 'show_indexes': True}),
    ] + urlpatterns

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        # Debug toolbar is explicitly linked, no magic that breaks on first request errors.
        import debug_toolbar
        urlpatterns.insert(0, url(r'^__debug__/', include(debug_toolbar.urls)))
