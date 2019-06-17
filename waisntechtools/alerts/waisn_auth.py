from functools import wraps
from os import environ

from django.contrib.auth.decorators import login_required

from waisntechtools.settings import DEBUG

_AUTH_DISABLED_KEY = 'WAISN_AUTH_DISABLED'
_AUTH_DISABLED_VALUE = 'TRUE'


def waisn_auth(view_func):
    """
    Decorator for views that performs authentication. Authentication can be disabled based on the environment settings.
    """
    @wraps(view_func)
    def _waisn_auth_decorator(request, *args, **kwargs):
        if _AUTH_DISABLED_KEY in environ and environ[_AUTH_DISABLED_KEY] == _AUTH_DISABLED_VALUE and DEBUG:
            return view_func(request)
        else:
            return login_required()(view_func)(request, *args, **kwargs)

    return _waisn_auth_decorator
