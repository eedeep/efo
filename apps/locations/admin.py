from django.contrib import admin
from django.db.models import get_model


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'venue',
    )
    
    prepopulated_fields = {"slug": ("venue",)}

admin.site.register(get_model('locations', 'location'), LocationAdmin)