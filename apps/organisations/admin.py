from django.contrib import admin
from django.db.models import get_model

from base.admin import BaseAdmin
from organisations.forms import OrganisationAdminModelForm

class OrganisationAdmin(BaseAdmin):
    
    filter_horizontal = (
        'organisation_type', 
        'organisation_expertise',
        'tags',)
    
    def content(self, obj):
        pass
    content.short_description = 'Description'
    content.verbose_name = 'Description'
    
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'summary',
                'content',
                'organisation_type',
                'organisation_expertise' )
        }),
        ('Contact', {
            'fields': (
                'phone', 
                'fax', 
                'mobile',
                'email',
                'website',
                'website_name',
                )
        }),
        ('Location', {
            'fields': (
                'street', 
                'suburb',
                'city', 
                'country',
                'state',
                'post_code',
                )
        }),
        ('Logo', {
            'fields': (
                'logo_image',
                )
        }),
        ('Meta', {
            'fields': (
                'is_published',
                'published',
                'tags',
                )
        }),
    )
    
    list_display = (
        'title',
        'country',
        'created',
        'modified',
        'published',
        'is_published'
    )
    
    list_filter = (
        'sites',
        'country'
    )
    
    search_fields = (
        'title',
    )    

    list_editable = (
        'is_published',
    )
    
    form = OrganisationAdminModelForm
    
admin.site.register(get_model('organisations', 'organisation'), OrganisationAdmin)

class OrganisationTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(get_model('organisations', 'organisationtype'), OrganisationTypeAdmin)

class OrganisationExpertiseAdmin(admin.ModelAdmin):
    pass
admin.site.register(get_model('organisations', 'organisationexpertise'), OrganisationExpertiseAdmin)