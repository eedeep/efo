from django.shortcuts import redirect, get_object_or_404, get_list_or_404, _get_queryset
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponseRedirect

from regions.models import Region

from os.path import join

def _get_object_list(klass, *args, **kwargs):
    """
    Builds on Django's private method _get_queryset
    Helps to DRY up a few things here
    """
    queryset = _get_queryset(klass)
    return list(queryset.filter(*args, **kwargs))
    
def _get_distinct_object_list(klass, *args, **kwargs):
    """
    Builds on Django's private method _get_queryset
    Helps to DRY up a few things here
    """
    queryset = _get_queryset(klass)
    return list(queryset.filter(*args, **kwargs).distinct())

def no_region_redirect(request):
    path_parts = request.path.split("/")
    redirect_to = "/" + "/".join(path_parts[2:])
    return redirect(redirect_to) # TODO: this doesn't seem to go?
    
def get_country_codes():
    return Region.objects.all().values_list("country_code") or None
    
def get_active_country_codes(klass, *args, **kwargs):
    #_get_distinct_object_list(klass, *args, **kwargs)
    # TODO: finish this
    return Region.objects.all().values_list("country_code") or None
    
def get_region(country_code):
    try:
        return Region.objects.get(country_code=country_code)
    except ObjectDoesNotExist:
        return None

def get_default_regions():
    return Region.objects.filter(default=True) or None
    
def get_list_by_region_or_404(klass, country_code, *args, **kwargs):
    kwargs.update({
        'regions': get_region(country_code),
    })
    return get_list_or_404(klass, *args, **kwargs)    

def get_object_by_region_or_404(klass, country_code, *args, **kwargs):
    kwargs.update({
        'regions': get_region(country_code),
    })
    return get_object_or_404(klass, *args, **kwargs)  
   
def get_list_by_region_or_redirect(klass, country_code, request, *args, **kwargs):
    """
    If a list of objects by Region are not available, redirect
    to either a specified URL, or to the same URL, without
    the country code path prefix
    """
    
    kwargs.update({
        'regions': get_region(country_code),
    })
    
    obj_list = _get_object_list(klass, *args, **kwargs)
    
    if not obj_list:
        no_region_redirect(request)  
    return obj_list    
    
def get_list_by_region_default_or_all(klass, country_code, request, *args, **kwargs):
    """
    Try to find a list of objects by region.
    If none found, try to find 'non-region' objects.
    If still none found, raise 404.
    
    find: region, default, all or None
    find: region or None
    find: all or None
    find: default or all or None
    find: default or None
    
    detect: geoip
        if au or nz:
            region or None
            region or default or all or None
    """
    
    if country_code:
        """
        We have a country code, so try to get a matching region.
        """
        try:
            region = Region.objects.get(country_code=country_code)
        except ObjectDoesNotExist:
            """
            No region is found, possibly the country_code is
            incorrect, or some other possibility.  So redirect
            to the region agnostic version of the URL.
            
            e.g.
                /au/app_name/  becomes
                /app_name/
            """
            no_region_redirect(request)
        else:
            kwargs.update({
                'regions': region,
            })
    else:
        """
        No country code is present, so look for
        default regions.
        """
        regions = get_default_regions()
        if regions:
            """
            If regions are found, update kwargs, otherwise
            attempt to retrieve a list of objects
            """
            kwargs.update({
                'regions__in': regions
            }) 
        """
        Otherwise, no default regions are found, so .all() will
        be attempted.
        """
    return _get_distinct_object_list(klass, *args, **kwargs)
        
 
    
