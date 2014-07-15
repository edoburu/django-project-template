from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from filebrowser.sites import site as fb_site
from fluent_blogs.sitemaps import EntrySitemap, CategoryArchiveSitemap, AuthorArchiveSitemap, TagArchiveSitemap
from fluent_pages.sitemaps import PageSitemap
from frontend.views import TextFileView, Http500View

admin.autodiscover()

sitemaps = {
    # Place sitemaps here
    'pages': PageSitemap,
    'blog_entries': EntrySitemap,
    'blog_categories': CategoryArchiveSitemap,
    'blog_authors': AuthorArchiveSitemap,
    'blog_tags': TagArchiveSitemap,
}

urlpatterns = patterns('',
    # Django admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(fb_site.urls)),
    url(r'^admin/util/tags/', include('taggit_autosuggest.urls')),
    url(r'^admin/util/tools/', include('admin_tools.urls')),
    url(r'^admin/util/tinymce/', include('tinymce.urls')),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),

    # SEO API's
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),

    # TODO: add your urls here

    # CMS modules
    url(r'^blog/comments/', include('fluent_comments.urls')),
    url(r'', include('fluent_pages.urls')),
)

if settings.DEBUG:
    urlpatterns.insert(0,
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
