from django.views.generic import TemplateView, View


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
