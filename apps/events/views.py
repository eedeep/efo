from django.core.urlresolvers import reverse
from django.db.models import Max, Min, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from base.utils import filter_by_getvalues
from popularity.signals import view

from events.models import Event, EventType

import dateutil.parser as dateparser
import datetime

def index(request):
    
    events = get_list_or_404(Event, is_published=True)
    
    return render_to_response(
        'events/index.html',
        {
            "events": events,
        },
        context_instance=RequestContext(request))
        
def event(request, event_id=None, slug=None,):
    
    event = get_object_or_404(Event, slug=slug, is_published=True)
    
    location = u'%s %s' % (event.street, event.city)
    
    # import ipdb; ipdb.set_trace()
    
    view.send(event)
    
    return render_to_response(
        'events/event.html',
        {
            "event": event,
            "location": location.split(),
        },
        context_instance=RequestContext(request))
        
def events(request):
    
    date = request.GET.get("date", False)
    if not date:
        date = datetime.date.today()
    else:
        date = dateparser.parse(date).date()
    filter_date = date
    
    query = Q(end_date__gte=date) | Q(start_date__gte=date)
    event_kwargs = {
        'is_published': True,}

    if request.GET.get('type'):
        event_kwargs.update({
            "event_type__slug": request.GET['type'].lower(),})
    if request.GET.get('location'):
        event_kwargs.update({
            "city": request.GET['location'],})
        
    events = Event.site_objects.filter(query, **event_kwargs).order_by('start_date')
    event_types = EventType.objects.filter(slug__in=events.values_list('event_type__slug'))
    
    locations = sorted(events.values('city', 'country'))
    
    if events:
        """
        Find the start date
        """
        # start with today, filter date, or the earliest event start date, or end date
        min_start_date = events.aggregate(Min('start_date'))['start_date__min']
        min_end_date = events.aggregate(Min('end_date'))['end_date__min']
    
        min_event_date = min_start_date if min_start_date < min_end_date else min_end_date
    
        # Only start with the event date if its greater than the date
        start_date = date if date > min_event_date else min_event_date
    
        """
        Find the end date
        """
        max_start_date = events.aggregate(Max('start_date'))['start_date__max']
        max_end_date = events.aggregate(Max('end_date'))['end_date__max']
    
        max_event_date = max_start_date if max_start_date > max_end_date else max_end_date
    
        """
        Loop through dates from start_date to end_date
        attaching events if they're a match.
        """
        current_date = start_date
        event_dates = []
        query = Q(start_date__lte=current_date) | Q(end_date__gte=date)
    
        while (current_date <= max_event_date):
        
            query = \
                Q(start_date=current_date) | \
                Q(start_date__lte=current_date) & Q(end_date__gte=current_date)
            current_date_events = events.filter(query).distinct()
            
            if current_date_events:
                event_date = {
                    "date": current_date,
                    # "qualifier": 'today' if current_date == datetime.date.today()
                    "events": current_date_events,}
                event_dates.append(event_date)
                current_date_events = []
            current_date = current_date + datetime.timedelta(days=1)
            # print current_date
    else:
        event_dates = []
        current_date = None
    
    return render_to_response(
        'events/events.html',
        {
            "current_date": current_date,
            "filter_date": filter_date,
            "event_dates": event_dates,
            "event_types": event_types,
            "locations": locations
        },
        context_instance=RequestContext(request))