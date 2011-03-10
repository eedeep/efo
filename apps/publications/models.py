from django.conf import settings
from django.db import models
from filebrowser.fields import FileBrowseField
from meta.utils import SlugifyUniquely # move to 'entropy'
import os

MONTHS = (
    ('Jan', 'Jan'),
    ('Feb', 'Feb'),
    ('Mar', 'Mar'),
    ('Apr', 'Apr'),
    ('May', 'May'),
    ('Jun', 'Jun'),
    ('Jul', 'Jul'),
    ('Aug', 'Aug'),
    ('Sep', 'Sep'),
    ('Oct', 'Oct'),
    ('Nov', 'Nov'),
    ('Dec', 'Dec'),
)

YEARS = (
    ('1995', '1995'),
    ('1996', '1996'),
    ('1997', '1997'),
    ('1998', '1998'),
    ('1999', '1999'),
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
)

COVER_IMAGE_PATH = os.path.join('images', 'magazine_covers')

class Publication(models.Model):
    """
    A Publication
    """
    title = models.CharField(
        max_length=200)
    slug = models.SlugField(
        blank=False,
        editable=False,
        max_length=250,
        unique=True)

    class Meta:
        abstract = True # For now.
    
    def __unicode__(self):
        return u'%s' % (self.title)
    
    def save(self, *args, **kwargs):
        if not self.id:
            """
            Replace self.title with your prepopulate_from field
            """
            self.slug = SlugifyUniquely(self.title, self.__class__)
        super(Publication, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return (str(self.content_type()) + '_view', (), {
            'magazine_slug': self.slug,
        })
    
class Magazine(Publication):
    """
    A Magazine, a type of Publication
    """
    content = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True)
    show_issues = models.BooleanField(blank=True, default=True)
    
    is_bimonthly = models.BooleanField(
        "Bi-monthly?",
        default=False,
        help_text="This magazine is published every two months")

    def has_feature_image(self):
        if self.magazineissue_set.all().count() > 0 and self.magazineissue_set.all()[0].cover_image:
            return True
        else:
            return False

    def feature_image(self):
        latest_issue = self.magazineissue_set.all().order_by('-issue_year', '-issue_number')[0]
        if latest_issue.cover_image_exists():
            rv = latest_issue.cover_image
        else:
            rv = latest_issue.placeholder_image_url()
        return rv
    
    def content_type(self):
        return u'magazine'
    
class MagazineIssue(models.Model):
    """
    A Magazine Issue
    """
    magazine = models.ForeignKey(
        Magazine)
        
    issue_name = models.CharField(
        blank=True,
        null=True,
        max_length=255)

    slug = models.SlugField(
        blank=False,
        editable=False,
        max_length=250,
        null=False,
        unique=True)
    
    issue_date = models.DateField(
        blank=True,
        editable=False,
        null=True)
        
    issue_number = models.PositiveIntegerField(
        blank=True, 
        null=True)
        
    issue_volume = models.PositiveIntegerField(
        blank=True,
        null=True)
        
    issue_month = models.CharField(
        blank=True,
        choices=MONTHS, 
        max_length=100,
        null=True)
    
    issue_year = models.CharField(
        blank=True,
        choices=YEARS,
        max_length=10,
        null=True)
        
    cover_image = FileBrowseField(
        "Issue cover", 
        blank=True,
        directory="covers", 
        max_length=250,
        null=True)
        
    class Meta:
        order_with_respect_to = 'magazine'
        ordering = [
            'magazine', '-issue_year', '-issue_number',]
            
        # unique_together = [ 'issue_year', issue_name]
    
    def __unicode__(self):
        display_name_fields = [
            self.magazine.title,
            self.issue_name,
            self.issue_month,
            self._next_month,
            self.issue_year ]
        display_name_values = []

        for display_name_field in display_name_fields:
            if display_name_field:
                display_name_values.append(display_name_field)
        return u'%s' % (' '.join(display_name_values))

    @property
    def _next_month(self):
        if self.magazine.is_bimonthly:
            try:
                index = MONTHS.index((self.issue_month, self.issue_month))
            except:
                return None
            else:
                if index == (len(MONTHS) - 1):
                    return MONTHS[0][0]
                else:
                    return MONTHS[index + 1][0]
        else:
            return None

    @property       
    def _display_month(self):
        if self._next_month:
            return u'%s/%s' % (self.issue_month, self._next_month)
        else:
            self.issue_month
            
    def save(self, *args, **kwargs):
        if not self.id:
            if self.issue_name:
                sluggable_string = self.issue_name
            else:
                sluggable_fields = [
                    self.magazine.title,
                    self.issue_month,
                    self._next_month,
                    self.issue_year,
                    self.issue_number]
                sluggable_string_values = []
                for sluggable_field in sluggable_fields:
                    if sluggable_field:
                        sluggable_string_values.append(sluggable_field)
                        
                sluggable_string = ' '.join(sluggable_string_values)
            
            self.slug = SlugifyUniquely(sluggable_string, self.__class__)
        super(MagazineIssue, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return (str(self.content_type()) + '_view', (), {
            'issue_slug': self.slug,
            'magazine_slug': self.magazine.slug
        })
        
    def content_type(self):
        return u'magazine_issue'
    
    def cover_image_exists(self):
        if self.cover_image and os.path.exists(os.path.join(settings.MEDIA_ROOT,self.cover_image.path_relative)):
            return True
        return False

    def placeholder_image_url(self):
        return settings.MAGAZINE_COVER_PLACEHOLDER_IMAGE_PATH

    def is_from_the_archive(self):
        if self.archivearticle_set.all().count() > 0:
            return True;
        return False;
    
    def issue_display_name(self):
        if self.issue_name:
            return u'%s' % (self.issue_name)
        else:
            display_name_fields = [
                self._display_month,
                self.issue_year ]
            display_name_values = []
        
            for display_name_field in display_name_fields:
                if display_name_field:
                    display_name_values.append(display_name_field)
                
        return u'%s' % (' '.join(display_name_values))
            
