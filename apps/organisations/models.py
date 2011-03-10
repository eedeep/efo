import os

from django.db import models

from base.models import OrganisationBase, BaseType
from filebrowser.fields import FileBrowseField
from locations.models import Location
from taggit.managers import TaggableManager

from settings import FEATURED_COUNTRIES

class OrganisationType(BaseType):
    pass

class OrganisationExpertise(BaseType):
    
    class Meta:
        verbose_name_plural = "organisation expertise"

class Organisation(OrganisationBase):
    """
    Organisation
    """
    
    organisation_type = models.ManyToManyField(
        OrganisationType, blank=True, null=True)
        
    organisation_expertise = models.ManyToManyField(
        OrganisationExpertise, blank=True, null=True)
    
    #Where
    street = models.CharField(max_length=200, blank=True)
    suburb = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200,
        blank=True, choices=FEATURED_COUNTRIES)
    state = models.CharField(max_length=200, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    
    phone = models.CharField(blank=True, max_length=100)
    fax = models.CharField(blank=True, max_length=100)
    mobile = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True, verify_exists=False)
    website_name = models.CharField(max_length=200, blank=True)
        
    logo_image = FileBrowseField(
        "Organisation logo", 
        blank=True,
        directory="logos/", 
        max_length=200,
        null=True)
    
    
    def __unicode__(self):
        return u'%s' % (self.title)
        
    def logo_title(self):
        return u'%s %s' % (self.title)