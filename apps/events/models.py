from django.db import models

from taggit.managers import TaggableManager

from base.models import EventBase, BaseType
from locations.models import Location

from settings import FEATURED_COUNTRIES
import datetime

class EventType(BaseType):
    pass

class Event(EventBase):
    
    #Event
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)
    
    event_type = models.ForeignKey(EventType, blank=True, null=True)
    
    #Contact Details
    phone = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)
    mobile = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    website_name = models.CharField(max_length=200, blank=True)
    
    #Where
    venue = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    suburb = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, 
        blank=True,
        choices=FEATURED_COUNTRIES)
    state = models.CharField(max_length=200, blank=True)
    post_code = models.CharField(max_length=200, blank=True)
    
    
    # tags = TaggableManager()