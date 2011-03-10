from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import truncate_words

from articles.models import Article, ArticleType
from colophon.models import Publisher

from legacy.models import \
    ArticlesArticle, \
    ArticlesArticleTags, \
    ArticlesArticletype, \
    ImagesArticleimage, \
    ImagesImage, \
    PublicationsMagazineissue, \
    TaggitTag

from meta.utils import SlugifyUniquely
from projects.models import Project
from imagess.models import ArticleImage as OldArticleImage
from publications.models import MagazineIssue
from images.models import ArticleImage
from taggit.models import Tag

# class ImagesImage(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=200)
#     slug = models.CharField(max_length=50)
#     caption = models.TextField()
#     image = models.CharField(max_length=100)
#     feature = models.BooleanField()
#     slide_show = models.BooleanField()
#     class Meta:
#         db_table = u'images_image'
# 
# class ImagesArticleimage(models.Model):
#     image_ptr = models.ForeignKey(ImagesImage)
#     article = models.ForeignKey(ArticlesArticle)
#     class Meta:
#         db_table = u'images_articleimage'

class Command(BaseCommand):
    help = 'migrate articles'

    def handle(self, *args, **options):
        images = ArticleImage.objects.all()
        for image in images:
            image.slug = SlugifyUniquely(truncate_words(image.caption, 4), ArticleImage)
            image.save()