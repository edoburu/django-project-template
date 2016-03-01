from django.views.generic import View


class Http500View(View):
    """
    A view which tests the error handling.
    """
    def get(self, request, *args, **kwargs):
        raise NotImplementedError("500 error page test")
