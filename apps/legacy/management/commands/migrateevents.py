from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from legacy.models import EventsEvent, EventsEventtype
from events.models import Event, EventType

class Command(BaseCommand):
    help = 'migrate events'

    def handle(self, *args, **options):
        """
        Events
        """
    
        l_events = EventsEvent.objects.all()
    
        user = User.objects.get(pk=1)
    
        for l_event in l_events:
        
            try:
                event_type = EventType.objects.get(pk=l_event.event_type.id)
            except:
                event_type = None
            
            kwargs = {
                'city': l_event.city,
                'content':  l_event.content,
                'country': l_event.country,
                'created': l_event.created,
                'created_by': user,
                'email': l_event.email,
                'end_date': l_event.end_date,
                'event_type': event_type,
                'fax': l_event.fax,
                'is_published': l_event.is_published,
                'mobile': l_event.mobile,
                'phone': l_event.phone,
                'post_code': l_event.post_code,
                'published': l_event.published,
                'slug': l_event.slug,
                'start_date': l_event.start_date,
                'state': l_event.state,
                'street': l_event.street,
                'suburb': l_event.suburb,
                'summary': l_event.summary,
                'title': l_event.title,
                'venue': l_event.venue,
                'website': l_event.website,
                'website_name': l_event.website_name,
            }
        
            event = Event(**kwargs)
        
            try:
                event.full_clean()
                # pass
            except ValidationError, e:
                # Do something based on the errors contained in e.message_dict.
                # Display them to a user, or handle them programatically.
                print e
            else:
                print event
                # event.save()