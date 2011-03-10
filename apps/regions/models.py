from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

import datetime

REGION_CACHE = {}

"""
    TODO.
        Model Region on the django sites framework
        where relevant.
"""

class Region(models.Model):
    """
    Region
    
        Extends the Django sites framework to allow
        for regions specified by country codes found
        in the url.
        
        i.e.
        
        domain.com/au
        domain.com/nz
    """
    site = models.ForeignKey(Site)
    country_code = models.SlugField(max_length=10) 
    default = models.BooleanField(
        help_text="Default region content"
    )
    
    def __unicode__(self):
        return "%s/%s/" % (self.site, self.country_code)
    
    