from django.db import models
from articles.models import MagazineSection
from publications.models import MagazineIssue 
from filebrowser.fields import FileBrowseField
from django.conf import settings
from django.template.defaultfilters import striptags
from django.utils.html import escape
import re
import string

class ArchiveArticle(models.Model):
    """
    An article from the existing Architecture Australia archive.
    """
    
    title = models.CharField(
        max_length=600)
    slug = models.CharField(
        max_length=255)
    
    content = models.TextField()
    
    magazine_section = models.ForeignKey(
        MagazineSection,
        blank=False,
        help_text="Associate this archive article with a magazine section.",
        null=False, )
        
    page_number = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0)
        
    introduction = models.TextField(
        blank=True)
        
    issue = models.ForeignKey(
        MagazineIssue,
        blank=False,
        null=False)

    credit = models.TextField(
        blank=True)

    review = models.TextField(
        blank=True)

    type_string = models.TextField()

    summary = models.TextField(
        blank=True)
        
    def __unicode__(self):
        return u'%s' % self.title

    def has_sections(self):
        """
        True if an article is made up of sections 
        """
        if self.archivearticlesection_set.count() > 0:
            return True
        else:
            return False

    def stripped_summary(self):
        stripped_summary = striptags(self.introduction).replace('&nbsp;', '').strip()

        whitespace_pattern = re.compile('^\s*$')
        if not stripped_summary or whitespace_pattern.match(stripped_summary):
            if self.has_sections():
                stripped_summary = self.archivearticlesection_set.all()[0].body
            else:   
                stripped_summary = self.content

            stripped_summary = striptags(stripped_summary).replace('&nbsp;','').strip()[0:settings.ARTICLE_SUMMARY_LENGTH] + '...'
                
        return stripped_summary

    def content_type(self):
        """
        To help in templates.
        """
        return self._meta.module_name

    class Meta:
        db_table = u'archive_article'


class ArchiveArticleSection(models.Model):

    archive_article = models.ForeignKey(
        ArchiveArticle,
        blank=False,
        null=False )

    heading = models.TextField(
        blank=True,
        null=True)

    bold_text = models.TextField(
        blank=True,
        null=True)

    body = models.TextField()

    author_description = models.TextField(
        blank=True,
        null=True)

    orig_body = models.TextField()

    template = models.IntegerField()

    class Meta:
        db_table = u'archive_articlesection'


class ArticleSectionImage(models.Model):

    archive_article_section = models.ForeignKey(
        ArchiveArticleSection,
        blank=False,
        null=False)

    url = FileBrowseField(
        "Archive article section image", 
        blank=True,
        directory="aa_archive_images", 
        max_length=250,
        null=True)

    sequence = models.IntegerField()

    caption = models.TextField(
        blank=True,
        null=True)
        
    def __unicode__(self):
        return u'%s' % self.url
