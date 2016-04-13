import admin_tools.urls
import django.contrib.sitemaps.views
import django.views.defaults
import django.views.static
import fluent_comments.urls
import fluent_pages.urls
import ping.urls
import taggit_autosuggest.urls
import tinymce.urls

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.functional import curry
from filebrowser.sites import site as fb_site
from fluent_blogs.sitemaps import EntrySitemap, CategoryArchiveSitemap, AuthorArchiveSitemap, TagArchiveSitemap
from fluent_pages.sitemaps import PageSitemap
from fluent_pages.views import RobotsTxtView
from os import path
from frontend.views import Http500View

sitemaps = {
    # Place sitemaps here
    'pages': PageSitemap,
    'blog_entries': EntrySitemap,
    'blog_categories': CategoryArchiveSitemap,
    'blog_authors': AuthorArchiveSitemap,
    'blog_tags': TagArchiveSitemap,
}

urlpatterns = [
    # Django admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(fb_site.urls)),
    url(r'^admin/util/tags/', include(taggit_autosuggest.urls)),
    url(r'^admin/util/tinymce/', include(tinymce.urls)),
    url(r'^admin/util/tools/', include(admin_tools.urls)),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^400/$', curry(django.views.defaults.bad_request, exception=None)),
    url(r'^403/$', curry(django.views.defaults.permission_denied, exception=None)),
    url(r'^404/$', curry(django.views.defaults.page_not_found, exception=None)),
    url(r'^500/$', django.views.defaults.server_error),

    # SEO API's
    url(r'^sitemap.xml$', django.contrib.sitemaps.views.sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', RobotsTxtView.as_view()),

    # Monitoring API's
    url(r'^api/ping/', include(ping.urls)),

    # TODO: add your urls here

    # CMS modules
    url(r'^blog/comments/', include(fluent_comments.urls)),
    url(r'', include(fluent_pages.urls)),
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
        urlpatterns.insert(0,
            url(r'^__debug__/', include(debug_toolbar.urls))
        )
