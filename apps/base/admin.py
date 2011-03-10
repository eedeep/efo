from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model
from django.shortcuts import _get_queryset


import datetime

def update_publishing_meta(request, obj, klass, change, save_object=True):
    """
    Base model 'admin' utility to auto update meta fields

        Assuming that the following fields are present
            created_by
            created
            modified_by
            modified
            published_by
            published
    """

    if not obj.id:
        obj.created_by = request.user
        obj.created = datetime.datetime.now()
        # ipdb.set_trace()
        if obj.is_published:
            # If the object is being created, and published
            obj.published_by = request.user
            obj.published = datetime.datetime.now()
    else:
        if change:
            obj.modified_by = request.user
            obj.modified = datetime.datetime.now()

    # If status is now 'published', changing from 'draft'
    # make published_by the current admin user
    if obj.is_published:
        # import pdb; pdb.set_trace()
        try:
            if not _get_queryset(klass).get(pk=obj.id).is_published:
                obj.published_by = request.user
                obj.published = datetime.datetime.now()
        except ObjectDoesNotExist:
            pass
    else:
        obj.published_by = None
        obj.published = None
        
    if save_object:
        obj.save()
    
def update_person_meta(request, obj, klass, change, save_object=True):
    """
    Base model 'admin' utility to auto update person meta fields

        Assuming that the following fields are present
            joined 
        
    """

    if not obj.id:
        obj.joined = datetime.datetime.now()
        
    if save_object:
        obj.save()
        
class BaseAdmin(admin.ModelAdmin):
    
    def created_meta(self, obj):
        return u'%s<br> by %s' % (
            obj.created.strftime('%d %b %Y %H:%M'), 
            obj.created_by)
    created_meta.allow_tags=True
    created_meta.short_description= 'created'
    
    def modified_meta(self, obj):
        if obj.modified:
            return u'%s<br> by %s' % (
                obj.modified.strftime('%d %b %Y %H:%M'), 
                obj.modified_by)
        else:
            return u''
    modified_meta.allow_tags=True
    modified_meta.short_description= 'modified'
    
    def publishing_meta(self, obj):
        if obj.is_published:
            return u'%s<br> by %s' % (
                obj.published.strftime('%d %b %Y %H:%M'), 
                obj.published_by)
        else:
            return u''
    publishing_meta.allow_tags=True
    publishing_meta.short_description= 'published'
    
    def save_model(self, request, obj, form, change):
        update_publishing_meta(
            request, obj, self.model, change, True)
            
    class Media:
        css = { 
            'all': ['/site_media/static/admin_overrides/css/admin.css', ]
        }
        js = [
            '/site_media/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/site_media/static/admin/tinymce_setup/tinymce_setup.js',
            '/site_media/static/admin/filebrowser/js/TinyMCEAdmin.js',]
