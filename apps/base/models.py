# TODO: Change this file name to base.py

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from taggit.managers import TaggableManager
from taggit.models import Tag

from django.contrib.comments.models import Comment
from popularity.models import ViewTracker

from colophon.models import Publisher
from features.models import Feature, FeatureSet
from meta.utils import SlugifyUniquely # move to 'entropy'

import datetime

class BaseDictionaryNode(models.Model):
    """
    Base 'Dict' Node to fulfill 'label', 'value' needs.
    """
    label = models.CharField(max_length=200)
    value = models.TextField()
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s: %s' % (self.label, self.value)
        
class BaseTupleNode(models.Model):
    """
    For use in things like choices.
    """
    value = models.CharField(max_length=200)
    display = models.TextField()
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s' % (self.display)


class BaseType(models.Model):
    """
    Base 'Type' field, usualy related to via FK
    """
    name = models.CharField(
        max_length=200)
    name_plural = models.CharField(
        blank=True,
        max_length=200,
        null=True)
    slug = models.SlugField(
        editable=False,
        max_length=250,
        unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)
        
    class Meta:
        abstract = True
        
    @property
    def handle(self):
        """A convenience for admin
        """
        return self.slug
    def save(self, *args, **kwargs):  
        if not self.id:
            # replace self.name with your prepopulate_from field
            self.slug = SlugifyUniquely(self.name, self.__class__)
        super(BaseType, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return u'%s' % self.name
        
class BaseCategory(BaseType):
    """
    Base 'Category' field, usualy related to via M2M
    """
    
    class Meta:
        abstract = True

class Base(models.Model):
    """
    Article model
    """
    
    title = models.CharField(
        max_length=250)
    short_title = models.CharField(
        blank=True,
        help_text="A short title used in listings and navigation.",
        max_length=250)
    slug = models.SlugField(
        blank=False,
        editable=False,
        max_length=250,
        unique=True)
    summary = models.TextField(
        "Summary",
        blank=True,
        help_text="Summary used in listings & excerpts.  No formatting except for linebreaks.")
    introduction = models.TextField(
        "Intro",
        blank=True,
        help_text="Presented as a introduction to the content.  No formatting except for linebreaks.")
    content = models.TextField(
        "Body")
        
    created = models.DateTimeField(
        blank=True,
        editable=False,
        null=True)
    created_by = models.ForeignKey(
        User,
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_created_by",
        null=True)
        
    modified = models.DateTimeField(
        blank=True,
        editable=False,
        null=True)
    modified_by = models.ForeignKey(
        User,
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_modified_by",
        null=True)
    
    is_published = models.BooleanField(
        "Publish",
        help_text="Publish the content on sites selected below. Date and time will be added on Save.")
    published = models.DateTimeField(
        # editable=False,
        "Published on",
        blank=True, 
        help_text="Current date and time will be automatically assigned on publication if nothing else is specified.",
        null=True)
    published_by = models.ForeignKey(
        User, 
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_published_by",
        null=True)
    publisher = models.ForeignKey(
        Publisher,
        blank=True,
        help_text="Publisher or owner of this content",
        null=True,
        verbose_name="Published by")
        
    publish_on_AU = models.BooleanField()
    publish_on_NZ = models.BooleanField()
    
    sites = models.ManyToManyField(
        Site,
        blank=True, 
        help_text="Publishes this content on the selected sites.",
        null=True,
        verbose_name="Sites")
    objects = models.Manager()
    site_objects = CurrentSiteManager('sites')
    
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_tags")
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return "%s" % (self.title)
        
    @models.permalink
    def get_absolute_url(self):
        return (str(self.content_type()) + '_view', (), {
            'slug': self.slug,
        })
        
    @models.permalink  
    def get_list_url(self):
        return (str(self.content_type()) + 's_' + str(self.content_type()) + 's', (), {})
    
    def save(self, *args, **kwargs):
        if not self.id:
            """
            Replace self.title with your prepopulate_from field
            """
            self.slug = SlugifyUniquely(self.title, self.__class__)
        # else:
        #             # current sites
        #             sites_ids = []
        #             if self.publish_on_AU:
        #                 sites_ids.append(1)
        #             if self.publish_on_NZ:
        #                 sites_ids.append(2)
        #                 
        #             sites = Site.objects.filter(pk__in=sites_ids)
        #             self.sites = sites    
        super(Base, self).save(*args, **kwargs)
        
    def feature_image(self):
        try:
            # Return the first image as feature
            return self.feature_images()[0]
        except:
            """
            IndexError or others.
            """
            return None
            
    def has_feature_image(self):
        if len(self.feature_images())>0 and self.feature_images()[0].image:
            return True
        else:
            return False
        
    def has_slideshow(self):
        """
        Return true if the article has at least 2 slideshow images
        """
        return True if len(self.slideshow_images()) >= 2 else False 
        
    def content_type(self):
        """
        To help in templates.
        """
        return self._meta.module_name
        
    def comments(self):
        """
        Get the comments for this object, if any.
        """
        comments = []
        all_comments = Comment.objects.get_query_set()
        for comment in all_comments:
            if comment.is_removed == False and comment.content_object == self:
                comments.append(comment)
                
        return comments
        
    def comments_count(self):
        try:
            return u'%s' % len(self.comments())
        except:
            None
        
    def view_count(self):
        """
        From django-popularity, get the view count for the object.
        This is used to sort objects in a list view.
        """
        return ViewTracker.get_views_for(self)
        
    def popularity(self):
        """
        Relative popularity calculated as views/age
        """
        try:
            return self.view_count() / (datetime.datetime.now() - self.published).days
        except:
            None
            
    def photographers(self):
        """
        Get the photographers of images attached to the object
        """
        photographers = []
        for image in self.feature_images():
            if image.user_credit:
                photographer = image.user_credit
                try:
                    """
                    Assumes user has a profile
                    """
                    photographer.display_name = photographer.profile_set.all()[0].display_name()
                except IndexError:
                    pass
                photographers.append(photographer)
            if image.custom_credit:
                photographers.append(image.custom_credit)
        try:        
            return set(sorted(photographers, key=lambda photographer: photographer))
        except IndexError:
            return None
            
    def published_on(self):
        sites = []
        for site in self.sites.all():
            try:
                sites.append(site.siteprofile_set.all()[0].abbrieviation)
            except IndexError:
                pass 
        return sites
        
    def published_on_AU(self):
        try:
            AU = Site.objects.get(pk=1)
        except:
            pass
        else:
            try: 
                self.sites.get(pk=AU.id)
            except:
                return '<span>-</span>'
            else:
                return '<span>&#x2713;</span>'
    published_on_AU.allow_tags = True
    published_on_AU.short_description = 'AU'
        
    def published_on_NZ(self):
        try:
            NZ = Site.objects.get(pk=2)
        except:
            pass
        else:
            try: 
                self.sites.get(pk=NZ.id)
            except:
                return '<span>-</span>'
            else:
                return '<span>&#x2713;</span>'
    published_on_NZ.allow_tags = True
    published_on_NZ.short_description = 'NZ'
        
    def published_on_URBIS(self):
        try:
            URBIS = Site.objects.get(pk=3)
        except:
            pass
        else:
            try: 
                self.sites.get(pk=URBIS.id)
            except:
                return '<span>-</span>'
            else:
                return '<span>&#x2713;</span>'
    published_on_URBIS.allow_tags = True
    published_on_URBIS.short_description = 'URBIS'
        
class ArticleBase(Base):
    
    feature_sets = models.ManyToManyField(
        FeatureSet,
        blank=True,
        help_text="Feature this content on the selected sites and feature areas.  Note, the content must be published on the corresponding site to take effect.",
        null=True)
    
    # migrate this to authors
    users = models.ManyToManyField(User,
        blank=True,
        null=True,
        verbose_name="authors",
        related_name="%(app_label)s_%(class)s_authors")
    
    class Meta:
        abstract = True
    
    def authors(self):
        """
        Get the authors with displayable name
        """
        authors = []
        for author in self.users.all():
            try:
                """
                Assumes user has a profile
                """
                author.display_name = author.profile_set.all()[0].display_name()
            except IndexError:
                pass
            authors.append(author)
        try:       
            return set(sorted(authors, key=lambda author: author))
        except IndexError:
            return None
        
    def feature_images(self):
       """
       Resolve and return the appropriate feature images
       """
       return self.articleimage_set.all() #feature=True)
           
    def slideshow_images(self):
        """
        Return slideshow images.
        """
        # return self.articleimage_set.filter(slide_show=True).order_by('-feature')
        return self.articleimage_set.all()
        
class ProjectBase(Base):

    class Meta:
        abstract = True
        
    def feature_images(self):
        """
        Resolve and return the appropriate feature images
        """        
        return self.projectimage_set.all()#feature=True)
        
    def images(self):
        return self.projectimage_set.all()
        
class OrganisationBase(Base):
    
    class Meta:
        abstract = True
        
    def has_feature_image(self):
        if self.logo_image:
            return True
        else:
            return False    
        
    def feature_images(self):
        """
        Resolve and return the appropriate feature images
        """        
        return self.organisationimage_set.all()
        
    def images(self):
        return self.organisationimage_set.all()
        
class EventBase(Base):
    
    class Meta:
        abstract = True
        
    def feature_images(self):
        """
        Resolve and return the appropriate feature images
        """
        return self.eventimage_set.all()#feature=True)
    
    def images(self):
        return self.eventimage_set.all()

    
