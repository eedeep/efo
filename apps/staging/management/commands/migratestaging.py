from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import truncate_words

from articles.models import Article, ArticleType
from colophon.models import Publisher

class Command(BaseCommand):
    help = 'migrate articles'

    def handle(self, *args, **options):
        
        
        
        images = ArticleImage.objects.all()
        for image in images:
            image.slug = SlugifyUniquely(truncate_words(image.caption, 4), ArticleImage)
            image.save()