# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ArticlesArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=600)
    slug = models.CharField(max_length=150)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(null=True, blank=True)
    created_by_id = models.IntegerField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modified_by_id = models.IntegerField(null=True, blank=True)
    is_published = models.IntegerField(blank=True, null=True)
    published = models.DateTimeField(null=True, blank=True)
    published_by_id = models.IntegerField(null=True, blank=True)
    article_type_id = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    short_title = models.CharField(max_length=750)
    summary = models.TextField(blank=True, null=True)
    publisher_id = models.IntegerField(null=True, blank=True)
    issue_id = models.IntegerField(blank=True, null=True)
    credit = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    type_string = models.TextField(blank=True, null=True)
    class Meta:
        db_table = u'articles_article'

class ArticlesArticlesection(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    bold_text = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author_description = models.TextField(blank=True, null=True)
    class Meta:
        db_table = u'articles_articlesection'

class ArticlesArticlesectionimage(models.Model):
    section_id = models.IntegerField()
    url = models.CharField(max_length=765)
    sequence = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    class Meta:
        db_table = u'articles_articlesectionimage'

class PublicationsMagazine(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=600)
    slug = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=600)
    class Meta:
        db_table = u'publications_magazine'

class PublicationsMagazineissue(models.Model):
    id = models.IntegerField(primary_key=True)
    magazine_id = models.IntegerField(null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    issue_number = models.IntegerField(null=True, blank=True)
    issue_month = models.CharField(max_length=300, null=True, blank=True)
    issue_year = models.CharField(max_length=30, null=True, blank=True)
    cover_image = models.CharField(max_length=300, null=True, blank=True)
    class Meta:
        db_table = u'publications_magazineissue'
