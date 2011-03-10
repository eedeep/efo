from django.contrib.sites.models import Site
from django.db import models

from settings import PUBLISHER_COUNTRIES
from filebrowser.fields import FileBrowseField

"""
Colophon
========

A collection of models that give more information _about_
a Site, or its content, and the owners/publishers/managers
of its content
"""

class Country(models.Model):
    """
    A simple country model
    """
    name = models.CharField(
        "Country name",
        max_length=255)
        
    abbrieviation = models.CharField(
        "2 letter country code",
        max_length=10)
        
    class Meta:
        verbose_name_plural = 'Countries'   
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.abbrieviation)
    
class SiteGroup(models.Model):
    """
    A logical grouping of Sites
    """
    name = models.CharField(
        "Site group name",
        max_length=255)
        
    slug = models.SlugField(
        "Site group slug/handle",
        help_text="Once this is set, it should not be changed -- the templates of the site depend on it.",
        max_length=250,
        unique=True)
        
    def __unicode__(self):
        return u"%s" % (self.name)
    
class SiteProfile(models.Model):
    """
    Similar to User/Profile architecture, we're extending
    the ability to hold extra information about a site in 
    a SiteProfile
    """
    site = models.ForeignKey(
        Site,
        unique=True)
        
    site_group = models.ForeignKey(
        SiteGroup,
        editable=False,
        blank=True,
        null=True)
        
    slug = models.SlugField(
        "Site slug/handle",
        help_text="Once this is set, it should not be changed -- the templates of the site depend on it.",
        max_length=250,
        unique=True)
        
    name = models.CharField(
        "Site name",
        blank=True,
        help_text="The full site name.  May be different from the `display name` found in sites.",
        max_length=255)
    
    abbrieviation = models.CharField(
        "Site name abbrieviation",
        blank=True,
        help_text="Usually a 2 to 4 letter (5 max) accronym or abbreviation of the site name",
        max_length=5)
        
    country = models.ForeignKey(
        "Country",
        blank=True,
        null=True)
        
    def __unicode__(self):
        return u"%s" % (self.site)

class Publisher(models.Model):
    """
    A Publisher (house) may own or be responsible for publishing
    and managing a Site and its content.
    """
    
    name = models.CharField(
        "Publisher name",
        help_text="Such as Architecture Now or Urbis",
        max_length=255)
        
    short_name = models.CharField(
        "Publisher short name",
        blank=True,
        help_text="Short name or abbreviation, such as ANow, Urbis, used in navigation and field labels",
        max_length=255)
    
    country = models.CharField(
        choices=PUBLISHER_COUNTRIES,
        max_length=255)
        
    def __unicode__(self):
        return u'%s - %s' % (self.name, self.country)
