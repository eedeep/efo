from django.db import models
from django.contrib.contenttypes.models import ContentType

from taggit.models import Tag

class TopicalContent(models.Model):
    """
    Applicable 'Content Types' to be selected for Topics
    """
    content_type = models.ForeignKey(ContentType)
    
    class Meta:
        verbose_name_plural = "topical content"
    
    def __unicode__(self):
        return u'%s' % (self.content_type)

class Topic(models.Model):
    """
    A Topic is a feature 'Tag'
    """
    
    tag = models.ForeignKey(Tag, help_text="Topic as a 'feature tag'")
    
    # topical_content = models.ForeignKey(TopicalContent)
    
    active = models.BooleanField(
        help_text="This topic is active")
    
    # class Meta:
        # unique_together = ('tag', 'topical_content') # applicable?
    
    def __unicode__(self):
        return u'%s' % (self.tag)