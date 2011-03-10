from django import template

register = template.Library()

register = Library()

def olderthan(value, arg):
    """Formats a date as the time since that date (i.e. "4 days, 6 hours")."""
    from antony.utils.time import olderthan
    if not value:
        return u''
    try:
        if arg:
            return olderthan(value, arg)
        return olderthan(value)
    except (ValueError, TypeError):
        return u''
olderthan.is_safe = False

register.filter(olderthan)