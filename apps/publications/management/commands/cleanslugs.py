from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import truncate_words


from publications.models import MagazineIssue
from meta.utils import SlugifyUniquely

class Command(BaseCommand):
    help = 'missing slugs'

    def handle(self, *args, **options):
        """
        Restore missing slugs.
        """
        
        mis = MagazineIssue.objects.all()
        
        for mi in mis:

            sluggable_fields = [
                mi.magazine.title,
                mi.issue_month,
                mi._next_month]
            sluggable_string_values = []
            for sluggable_field in sluggable_fields:
                if sluggable_field:
                    sluggable_string_values.append(sluggable_field)
                
            sluggable_string = ' '.join(sluggable_string_values)
        
            mi.slug = SlugifyUniquely(sluggable_string, mi.__class__)
            print mi.slug