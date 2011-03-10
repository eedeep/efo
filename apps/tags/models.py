from django.db import models
from taggit.models import Tag

Tag._meta.ordering = ['name']
