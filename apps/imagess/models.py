import os

from django.db import models
from django.contrib.auth.models import User

from meta.utils import SlugifyUniquely

from articles.models import Article
from events.models import Event
from projects.models import Project

# import settings

IMAGE_PATH = os.path.join('images')

class Image(models.Model):
    """
    A very simple Image model.
    
    Not 'generic' at the moment... it might be soon?
    """
    
    title = models.CharField(blank=True, max_length=200)
    slug = models.CharField(
        blank=True,
        max_length=200)
        
    caption = models.TextField(blank=True)
    
    image = models.ImageField(upload_to='images')
    
    contributor = models.ManyToManyField(
        User,
        related_name="old_contributores",
        blank=True, null=True)
    
    feature = models.BooleanField(
        help_text="The 'feature' image")
    slide_show = models.BooleanField(
        help_text="Include this image in a slideshow")
    
    def __unicode__(self):
        return u'%s' % (self.image)
        
    
class ArticleImage(Image):
    article = models.ForeignKey(
        Article,
        to_field='old_id',
        related_name="old_article_images")
        
class ProjectImage(Image):
    project = models.ForeignKey(
        Project,
        to_field='old_id',
        related_name="old_project_images")
    