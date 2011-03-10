from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^event/(?P<slug>.*)$',
        'events.views.event',   
        name="event_view",
    ),
    url(
        r'^$', 
        'events.views.events',
        name="events_events"
    ),
)