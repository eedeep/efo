import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from filebrowser.fields import FileBrowseField
from meta.utils import SlugifyUniquely

from articles.models import Article
from events.models import Event
from projects.models import Project

class Image(models.Model):
    """
    A very simple Image model.
    
    Not 'generic' at the moment... it might be soon?
    """
    
    slug = models.SlugField(
        blank=True,
        editable=False,
        max_length=250)
        
    slide_show = models.BooleanField(
        "Include this image in the slideshow", 
        default=True)

    # image = models.ImageField(upload_to='images')
    image = FileBrowseField(
        "Image file", 
        blank=True,
        directory="images/", 
        max_length=200,
        null=True,
        help_text="Click thumbnail to view ful size image.")

    caption = models.TextField(blank=True)

    user_credit = models.ForeignKey(User,
        blank=True,
        null=True,
        verbose_name="User credit")

    custom_credit = models.CharField(
        blank=True,
        max_length=200,
        help_text="Add an image credit without the need to create a user.")
    
    order = models.PositiveSmallIntegerField(
        "Order",
        blank=True,
        null=True)
        
    # @@@ Deprecate ??
    feature = models.BooleanField(
        help_text="The 'feature' image")
        
    # @@@
    
    class Meta:
        ordering = ['order']
    
    def __unicode__(self):
        return u'%s' % (self.image)
        
    def save(self, *args, **kwargs):  
        if not self.id:
            self.slug = SlugifyUniquely(self.caption, self.__class__)
        super(Image, self).save(*args, **kwargs)
 
    def photographers(self):
        """
        Collect the user_credit and the custom_credit in a list
        """
        photographers = []
        
        if self.user_credit:
            photographer = self.user_credit
            try:
                # Assumes user has a profile
                photographer.display_name = photographer.profile_set.all()[0].display_name()
            except IndexError:
                pass
            photographers.append(photographer)
            
        if self.custom_credit:
            photographers.append(self.custom_credit)
            
        try:        
            return set(sorted(photographers, key=lambda photographer: photographer))
        except IndexError:
            return None

# Un-generic... :)
class ArticleImage(Image):
    article = models.ForeignKey(Article)
    
class EventImage(Image):
    event = models.ForeignKey(Event)
    
class ProjectImage(Image):
    project = models.ForeignKey(Project)

# South requires custom fields to be given "rules".
# See http://south.aeracode.org/docs/customfields.html
if "south" in settings.INSTALLED_APPS and "filebrowser" in settings.INSTALLED_APPS:
    try:
        from filebrowser.fields import FileBrowseField
        from south.modelsinspector import add_introspection_rules
        add_introspection_rules(rules=[((FileBrowseField,), [], {})],
                                      patterns=["filebrowser\.fields\."])
    except ImportError:
        pass
