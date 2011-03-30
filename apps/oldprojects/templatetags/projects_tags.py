from django import template
from django.utils.safestring import mark_safe, SafeData
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
# @stringfilter
def selector_search_links(value, splitter=';', autoescape=None):
    if not isinstance(value, SafeData):
        value = mark_safe(value)
    value = value.split(splitter)
    
    results = []
    for v in value:
        if v:
            results.append('<a href="http://selector.com/au/search?terms=%s" target="_blank">%s</a>' % (v.strip(), v.strip()))
        
    html = ', '.join(results)
    return mark_safe(html)
selector_search_links.is_safe = True
selector_search_links.needs_autoescape = True