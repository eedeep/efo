from django.db.models import get_model, Q
from django.shortcuts import get_list_or_404

from popularity.models import ViewTracker

import datetime
import dateutil.parser as dateparser

# @@@ call this get_filtered_list_or_404(request, klass) -- or create another version
def filter_by_getvalues(request, queryset):
    """
    Take a queryset and return a new one, depending on the GET
    filter variables present
    """
    
    # get model
    try:
        model = queryset[0]._meta.module_name
        app = queryset[0]._meta.app_label 
    except:
        # something was up... so just return the queryset
        return queryset
    
    if model == 'event':
        
        kwargs = {}
            
        try:
            if request.GET['type'] != '':
                kwargs.update({
                    "event_type__slug": request.GET['type']
                })
        except:
            pass
    
        try:
            if request.GET['location'] != '':
                kwargs.update({
                    "city": request.GET['location']
                })
        except:
            pass
            
        queryset = queryset.filter(**kwargs)
            
    else: # non-event
        
        # if the queryset is based on base.models
        if queryset[0].Meta.__module__ == 'base.models':
            """
            If this is true, then we know that we have the 
            publishing fields to work with.
            """
            try:
                if request.GET['order'] == 'recent':
                    # @@@   should be set to the default ordering, via latest(field_name=None)
                    #       so this is unecessary?
                    queryset.sort(key=lambda obj:obj.published, reverse=True)
                
                if request.GET['order'] == 'popular':
                    # sort the queryset by hits/popularity
                    # need to introduce the django tracking/logging app.
                    queryset.sort(key=lambda obj:obj.view_count(), reverse=True)
                if request.GET['order'] == 'discussed':
                    # sort the queryset by comments made
                    queryset.sort(key=lambda obj:obj.comments_count(), reverse=True)
            except:
                pass
                
            # ipdb.set_trace()
        
            # then impose a 'range' filter: week, month, year.
        
        
            try:
                if request.GET['range'] == 'all':
                    pass
            
                if request.GET['range'] == 'week':
                    last_week = datetime.date.today() - datetime.timedelta(days=7)
                    queryset = get_list_or_404(
                        get_model(app, model),
                        published__gte=last_week,
                        id__in=[obj.id for obj in queryset])
                    
                # get_model(app, model).objects.filter(published__gte=last_week, id__in=[obj.id for obj in queryset])
                # get_model(app, model).objects.filter(published__lte=last_week, id__in=[obj.id for obj in queryset])   
            
                if request.GET['range'] == 'month':
                    last_month = datetime.date.today() - datetime.timedelta(days=28)
                    queryset = get_list_or_404(
                        get_model(app, model), 
                        published__gte=last_month, 
                        id__in=[obj.id for obj in queryset])
            
                if request.GET['range'] == 'year':
                    last_year = datetime.date.today() - datetime.timedelta(days=365)
                    queryset = get_list_or_404(
                        get_model(app, model),
                        published__gte=last_year,
                        id__in=[obj.id for obj in queryset])
            except:
                pass
    
    return queryset
    
    
    