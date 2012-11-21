from django.views.generic.base import TemplateView

class TextFileView(TemplateView):
    """
    A ``TemplateView`` that sets the proper headers
    """
    content_type = 'text/plain'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = self.content_type
        context['ROOT_URL'] = self.request.build_absolute_uri('/')
        return super(TextFileView, self).render_to_response(context, **response_kwargs)
