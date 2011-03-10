from django.contrib import admin
from django.db.models import get_model

from base.admin import BaseAdmin
from images.admin import ImageInline
from events.forms import EventAdminModelForm

class EventImageInline(ImageInline):
    model = get_model('images', 'eventimage')

class EventAdmin(BaseAdmin):
    
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'short_title',
                'start_date',
                'end_date',
                'event_type',
                'summary',
                'introduction',
                'content',
            )
        }),
        ('Publishing', {
            'fields': (
                'is_published',
                'published',
                'publisher',
                'sites',
                )
        }),
        ('Contact Details', {
            'fields': (
                'phone', 
                'fax', 
                'mobile',
                'email',
                'website',
                'website_name',
                )
        }),
        ('Event Location', {
            'fields': (
                'venue',
                'street', 
                'city', 
                'suburb',
                'country',
                'state',
                'post_code',
                )
        }),
        ('Meta', {
            'fields': (
                'tags',
                )
        }),
    )
    
    filter_horizontal = ('tags',)
    form = EventAdminModelForm
    
    inlines = [
        EventImageInline,
    ]
    
    list_display = (
        'title',
        'is_published',
        'event_type',
        'start_date',
        'end_date',
        'city',
        'country',
    )
    list_editable = (
        'event_type',
        'start_date',
        'end_date',
        'city',
        'country',
    )
    list_filter = (
        'sites',
    )
    save_as = True
    search_fields = (
        'title',
    )

admin.site.register(get_model('events', 'event'), EventAdmin)

admin.site.register(get_model('events', 'eventtype'))
