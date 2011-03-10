from django import template

from events.models import Event

register = template.Library()

@register.inclusion_tag('base/_asides_object_list.html')
def latest_events():
    events = Event.site_objects.filter(is_published=True).order_by('-published')[0:3]
    return { 
        'objects': events,
    }
