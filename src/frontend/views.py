from os import path

from django.conf import settings
from django.views.generic import TemplateView, View
from django.views.static import serve

from {{ project_name }}.lib.http import far_future_expires

WEB_PATH = path.join(settings.ROOT_DIR, 'web')


class TextFileView(TemplateView):
    """
    A ``TemplateView`` that sets the proper headers
    """
    content_type = 'text/plain'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = self.content_type
        context['ROOT_URL'] = self.request.build_absolute_uri('/')
        return super(TextFileView, self).render_to_response(context, **response_kwargs)


class Http500View(View):
    """
    A view which tests the error handling.
    """

    def get(self, request, *args, **kwargs):
        raise NotImplementedError("500 error page test")


@far_future_expires()
def serve_web_file(request, path):
    """
    Quickly serve a file from the web folder.
    It will use the FileResponse, so invoke uWSGI's sendfile() via wsgi.file_handler
    """
    return serve(request, path, document_root=WEB_PATH)
