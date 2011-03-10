from django.contrib import admin
from django.db.models import get_model

from publications.forms import MagazineAdminModelForm

class MagazineIssueInline(admin.TabularInline):
    model = get_model('publications', 'magazineissue')
    extra = 1

class MagazineAdmin(admin.ModelAdmin):
    
    form = MagazineAdminModelForm
    
    inlines = [
        MagazineIssueInline,
    ]
    
    class Media:
        css = { 
            'all': ['/site_media/static/admin_overrides/css/admin.css', ]
        }
        js = [
            '/site_media/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/site_media/static/admin/tinymce_setup/tinymce_setup.js',
            '/site_media/static/admin/filebrowser/js/TinyMCEAdmin.js',]
    
admin.site.register(get_model('publications', 'magazine'), MagazineAdmin)
admin.site.register(get_model('publications', 'magazineissue'))