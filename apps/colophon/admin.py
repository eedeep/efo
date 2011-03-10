from django.contrib import admin
from django.db.models import get_model

class PublisherAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'short_name',
        'country',)
    
admin.site.register(get_model('colophon', 'publisher'), PublisherAdmin)

class SiteProfileAdmin(admin.ModelAdmin):
    
    list_display = (
        'site',
        'name',
        'abbrieviation',
        'country',)
        
    list_editable = (
        'name',
        'abbrieviation',
        'country',)
    
admin.site.register(get_model('colophon', 'siteprofile'), SiteProfileAdmin)
admin.site.register(get_model('colophon', 'country'))
