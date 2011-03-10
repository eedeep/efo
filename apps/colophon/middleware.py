from django.conf import settings
from django.contrib.sites.models import Site

class MultiHostMiddleware:

    def process_request(self, request):
        try:
            host_raw = request.META["HTTP_HOST"]
            colon = host_raw.find(':')
            if colon > -1:
                host = host_raw[0:colon]
            else:
                host = host_raw
            try:
                s = Site.objects.get(domain=host)
            except:
                settings.INTERNAL = True
            else:
                settings.INTERNAL = False
                if s:
                    settings.SITE_ID = s.id

        except KeyError:
            pass # use default urlconf (settings.ROOT_URLCONF)
            
    def process_response(self, request, response):
        
        response['INTERNAL'] = 'settings.INTERNAL'
        
        return response