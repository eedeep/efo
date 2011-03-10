from django.conf import settings

def multihost(request):

    return {
        'INTERNAL': settings.INTERNAL,
    }