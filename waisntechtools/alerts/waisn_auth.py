from functools import wraps

from django.conf import settings
from django.contrib.auth.decorators import login_required


def waisn_auth(view_func):
    """
    Decorator for views that performs authentication. Authentication can be disabled based on the environment settings.
    """
    @wraps(view_func)
    def _waisn_auth_decorator(request, *args, **kwargs):
        if settings.WAISN_AUTH_DISABLED and settings.DEBUG:
            return view_func(request)
        else:
            return login_required()(view_func)(request, *args, **kwargs)

    return _waisn_auth_decorator
