from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from colophon.models import SiteGroup

register = template.Library()

# All of this stuff should be moved to colophon or entropy?

@register.inclusion_tag('meta/site_select.html')
def site_select():
    sites = Site.objects.all()
    current_site = Site.objects.get_current()
    return { 
        "current_site": current_site,
        "sites": sites 
    }

@register.simple_tag
def current_site_country_code():
    current_site = Site.objects.get_current()
    try:
        return current_site.siteprofile_set.all()[0].country.abbrieviation
    except:
        return u'AU'
        
@register.simple_tag
def current_site_country():
    current_site = Site.objects.get_current()
    try:
        return current_site.siteprofile_set.all()[0].country.name
    except:
        return u'Australia'
        
@register.simple_tag
def current_site_name():
    current_site = Site.objects.get_current()
    try:
        return current_site.siteprofile_set.all()[0].name
    except:
        return u'Architecture Now'
        
@register.simple_tag
def current_site_slug():
    current_site = Site.objects.get_current()
    try:
        return current_site.siteprofile_set.all()[0].slug
    except:
        return u'anow-au'

@register.inclusion_tag('meta/site_nav_list.html')
def site_nav_list():
    sites = Site.objects.all().order_by('name')
    for site in sites:
        try:
            site.display_name = site.siteprofile_set.all()[0].country.abbrieviation
        except:
            site.display_name = site.name
    
    current_site = Site.objects.get_current()
    return { 
        "current_site": current_site,
        "sites": sites
    }
    
@register.inclusion_tag('meta/site_nav_list.html')
def site_group_nav_list():
    current_site = Site.objects.get_current()
    try:
        current_site_group = SiteGroup.objects.get(siteprofile__site=current_site)
    except ObjectDoesNotExist:
        sites = Site.objects.all().order_by('name')
    else:
        sites = Site.objects.filter(siteprofile__site_group=current_site_group).order_by('name')
    
    for site in sites:
        try:
            site.display_name = site.siteprofile_set.all()[0].country.abbrieviation
        except:
            site.display_name = site.name
    
    return { 
        "current_site": current_site,
        "sites": sites
    }

