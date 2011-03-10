from django.db import models

class Location(models.Model):
    """
    A simple Location model
    """
    
    venue = models.CharField(max_length=200)
    slug = models.SlugField()

    street_unit = models.CharField(blank=True, max_length=100)    
    street_number = models.CharField(blank=True, max_length=100)
    street = models.CharField(blank=True, max_length=100)
    street_suffix = models.CharField(
        help_text="such as: road, street, etc.",
        blank=True, max_length=200)
        
    city = models.CharField(blank=True, max_length=200)
    state = models.CharField(blank=True, max_length=200)
    post_code = models.CharField(
        help_text="Post or Zip code", blank=True, max_length=10)
        
    country = models.CharField(blank=True, max_length=200)
    
    def __unicode__(self):
        return u'%s' % (self.venue)
    
