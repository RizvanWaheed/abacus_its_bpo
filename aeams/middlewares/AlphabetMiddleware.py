from django.conf import settings
import time, logging
import re

logger = logging.getLogger("__name__")
EXEMPT_URLS = [settings.LOGIN_URL]
#EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [url for url in settings.LOGIN_EXEMPT_URLS]
    # EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class AlphabetMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code that is executed in each request before the view is called
        before_timestamp = time.time()
        logger.info(f"Tracking {before_timestamp}")

        response = self.get_response(request)
        # Code that is executed in each request after the view is called

        after_timestamp = time.time()
        delta = after_timestamp - before_timestamp
        logger.info(f"Tracking {after_timestamp} for a delta of {delta}")

        return response