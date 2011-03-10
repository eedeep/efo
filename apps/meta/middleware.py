from django.conf import settings

class AppMetaMiddleware(object):
    """
    Middleware that handles app Meta.
    """

    def process_response(self, request, response):
        """
        
        """
        return response