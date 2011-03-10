from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError

from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect

from base.utils import filter_by_getvalues
from popularity.signals import view

from events.models import Event, EventType

import dateutil.parser as dateparser
import datetime

from legacy.models import EventsEvent, EventsEventtype
from events.models import Event, EventType

import ipdb

class Command(BaseCommand):
    help = 'events'

    def handle(self, *args, **options):