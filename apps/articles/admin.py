from django.contrib import admin
from django.contrib.sites.models import Site
from django.db.models import get_model
from django.shortcuts import _get_queryset

from articles.forms import ArticleAdminModelForm
from base.admin import BaseAdmin
from images.admin import ImageInline
from images.forms import ImageAdminModelForm


import datetime


class ArticleImageInline(ImageInline):
    model = get_model('images', 'articleimage')
    form = ImageAdminModelForm

# actions

def publish_on_AU(modeladmin, request, queryset):
    sites = Site.objects.filter(pk=1)
    for obj in queryset:
        obj.sites = sites
        obj.save()
publish_on_AU.short_description = "Publish on AU"

def publish_on_NZ(modeladmin, request, queryset):
    sites = Site.objects.filter(pk=2)
    for obj in queryset:
        obj.sites = sites
        obj.save()
publish_on_NZ.short_description = "Publish on NZ"

class ArticleAdmin(BaseAdmin):
    
    actions = [publish_on_AU, publish_on_NZ]
        
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'short_title',
                'article_type',
                'magazine_section',
                'page_number',
                'users',
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
        ('Meta', {
            'fields': (
                'tags',
                'project',
                'issues',
                )
        }),)
    
    list_display = (
        'title',
        'article_type',
        'magazine_section',
        'format_modified',
        'format_published',
        #'is_published',
        'published_on_AU',
        'published_on_NZ',
        'published_on_URBIS',)

    list_filter = (
        'article_type',
        'sites',)
    
    search_fields = (
        'title',)    

    #list_editable = (
        #'is_published',)
    
    list_display_links = ()
    
    filter_horizontal = (
        'issues', 
        'tags', 
        'users',)
    
    form = ArticleAdminModelForm
    
    inlines = [
        ArticleImageInline, ]

    def format_published(self, obj):
        return obj.published.strftime('%d %b %Y')
    format_published.short_description = 'Published'
    format_published.admin_order_field = 'published'

    def format_modified(self, obj):
        return obj.published.strftime('%d %b %Y ')
    format_modified.short_description = 'Modified'
    format_modified.admin_order_field = 'modified'

    class Media:
        js = [
                '/site_media/static/js/anow/text-counter.js',
             ]
        
admin.site.register(get_model('articles', 'article'), ArticleAdmin)

class ArticleTypeAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'name_plural',
                'tags',)
        }),
        ('Navigation', {
            'fields': (
                'is_navigable',)
        }),
        ('Publishing', {
            'fields': (
                'is_published',)
        }),
        ('Legacy', {
            'fields': (
                'section',)
        }),)
        
    filter_horizontal = (
        'tags',)
    
    list_display = (
        'name',)
    
    list_display_links = ()
    
admin.site.register(get_model('articles', 'articletype'), ArticleTypeAdmin)
