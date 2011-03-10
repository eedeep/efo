from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def site_switch(request):
    """
    Dynamically set the site ID and return to the same url
    """
    
    site_id = request.POST.get("site_id", 1)
    
    settings.SITE_ID = site_id
    
    return HttpResponseRedirect(reverse('home'))
    