from datetime import datetime, timedelta
from functools import wraps


def far_future_expires(delta=timedelta(days=1)):
    """Decorator to set far-future expire headers."""

    def _decorator(view):
        @wraps(view)
        def _add_expires(request, *args, **kwargs):
            expiry_time = datetime.utcnow() + delta
            response = view(request, *args, **kwargs)
            response['Expires'] = expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
            return response

        return _add_expires

    if callable(delta):
        view = delta
        delta = timedelta(days=1)
        return _decorator(view)

    return _decorator
