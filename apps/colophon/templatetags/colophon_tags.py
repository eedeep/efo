from django.conf import settings
from django import template

from django.contrib.sites.models import Site

register = template.Library()

# All of this stuff should be moved to colophon or entropy?

@register.inclusion_tag('colophon/internal_site_switch.html')
def internal_site_switch():
    
    sites = Site.objects.all()
    current_site = Site.objects.get_current()
    is_internal = settings.INTERNAL
   
    return { 
        "current_site": current_site,
        "sites": sites,
        "is_internal": is_internal,
    }