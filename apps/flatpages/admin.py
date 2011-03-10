from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class FlatpageForm(forms.ModelForm):
    
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage
        widgets = {
            'content': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
        }


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')
    
    class Media:
        js = [
            '/site_media/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/site_media/static/admin/tinymce_setup/tinymce_setup.js',
            '/site_media/static/admin/filebrowser/js/TinyMCEAdmin.js',]
        

admin.site.register(FlatPage, FlatPageAdmin)
