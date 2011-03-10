from django import template
from django.utils.safestring import mark_safe, SafeData
from django.utils.encoding import smart_str, force_unicode
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def force_unicode(value):
    return mark_safe(force_unicode(value))
force_unicode.is_safe = True
# force_unicode.needs_autoescape = True