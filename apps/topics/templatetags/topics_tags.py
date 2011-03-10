from django import template

from topics.models import Topic

register = template.Library()

@register.inclusion_tag('topics/topics_nav_list.html')
def topics_nav_list():
    topics = Topic.objects.filter(active=True)
    return { "topics": topics }
