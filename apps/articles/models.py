import os

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from django.conf import settings

from base.models import ArticleBase, BaseType
from colophon.models import Publisher
from projects.models import Project
from publications.models import MagazineIssue
from taggit.managers import TaggableManager
from taggit.models import Tag

import calendar, datetime, popularity

class MagazineSection(models.Model):
    """
    Magazine section for an article
    """
    section_name = models.CharField(
        blank=False,
        null=False,
        max_length=255)

    def __unicode__(self):
        return u'%s' % (self.section_name)
        

class ArticleType(BaseType):
    """
    Article types
    """
    
    section = models.CharField(
        blank=True,
        choices=(
            ('news', 'news'),
            ('features', 'features'),
            ('blog', 'blog')),
        max_length=100)
        
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Feature tags",
        blank=True,
        help_text="Choose 'feature tags' that will be used as sub-navigation items to the parent Article Type",
        null=True)
        
    is_navigable = models.BooleanField(
        default=True,
        help_text="Include this article type as a Navigation item")
        
    is_published = models.BooleanField(
        default=True,
        help_text="Publish this article type throughout the site")
    
class Article(ArticleBase):
    """
    An article.
    """

    PLACEHOLDER_IMAGE_PATH = 'files/aa_archive_covers/placeholder.jpg'

    old_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        unique=True)
    
    article_type = models.ForeignKey(
        ArticleType, 
        help_text="This is the article type",
        null=True)
        
    issues = models.ManyToManyField(
        MagazineIssue,
        blank=True,
        verbose_name="Magazine references",
        null=True)
        
    project = models.ForeignKey(
        Project,
        blank=True,
        help_text="Associate this article with a Project.",
        null=True)

    magazine_section = models.ForeignKey(
        MagazineSection,
        blank=True,
        help_text="Associate this article with a magazine section.",
        null=True, 
    )

    page_number = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="An optional page number if this article also appears in a print magazine."
    )
        
        
    @property    
    def get_tags(self):
        return self.tags.all()
    
    @property    
    def get_magazines(self):
        return self.issues.all()

    def placeholder_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.PLACEHOLDER_IMAGE_PATH)

popularity.register(Article)
