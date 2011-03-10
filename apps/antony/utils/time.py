import datetime
import time

from django.utils.translation import ungettext, ugettext

def olderthan(d, age):
    
    """
    Check to see if a given date is older than an age duration supplied in 
    seconds
    """
    
    this_date = d
    
    chunks = (
      (60 * 60 * 24 * 365, lambda n: ungettext('year', 'years', n)),
      (60 * 60 * 24 * 30, lambda n: ungettext('month', 'months', n)),
      (60 * 60 * 24 * 7, lambda n : ungettext('week', 'weeks', n)),
      (60 * 60 * 24, lambda n : ungettext('day', 'days', n)),
      (60 * 60, lambda n: ungettext('hour', 'hours', n)),
      (60, lambda n: ungettext('minute', 'minutes', n))
    )
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(this_date, datetime.datetime):
        this_date = datetime.datetime(this_date.year, this_date.month, this_date.day)

    # Get 'now'
    now = datetime.datetime.now();
    delta = now - this_date #(this_date - datetime.timedelta(0, 0, this_date.microsecond))
    week = datetime.timedelta(seconds=604800)
    
    # ipdb.set_trace()
    
    # is greater than one week?
    if delta > week:
        return True
    else:
        return False