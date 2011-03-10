from django.contrib import admin
from django.contrib import databrowse
from django.db.models import get_model

from base.admin import BaseAdmin
from images.admin import ImageInline
from projects.forms import ProjectDetailsAdminModelForm, \
    ProjectProductsAdminModelForm, ProjectAdminModelForm
    
from projects.models import *
from images.models import *

class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    
    # prepopulated_fields = {"slug": ("name",)}

admin.site.register(get_model('projects', 'projecttype'), ProjectTypeAdmin)
databrowse.site.register(ProjectType)

admin.site.register(get_model('projects', 'projectroletype'))
databrowse.site.register(ProjectRoleType)

class ProjectSiteTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    
    # prepopulated_fields = {"slug": ("name",)}

admin.site.register(get_model('projects', 'projectsitetype'), ProjectSiteTypeAdmin)
databrowse.site.register(ProjectSiteType)

class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    
    # prepopulated_fields = {"slug": ("name",)}

admin.site.register(get_model('projects', 'projectcategory'), ProjectCategoryAdmin)
databrowse.site.register(ProjectCategory)

class ProjectStatusAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'display',
    )
    
    # prepopulated_fields = {"display": ("value",)}

admin.site.register(get_model('projects', 'projectstatus'), ProjectStatusAdmin)
databrowse.site.register(ProjectStatus)

class ProjectDetailInline(admin.TabularInline):
    model = get_model('projects', 'projectdetail')
    form = ProjectDetailsAdminModelForm
    extra = 1
    
databrowse.site.register(ProjectDetail)
    
class ProjectCompanyInline(admin.TabularInline):
    model = get_model('projects', 'projectcompany')
    extra = 1
    
databrowse.site.register(ProjectCompany)
    
class ProjectIndividualInline(admin.TabularInline):
    model = get_model('projects', 'projectindividual')
    extra = 1
    
databrowse.site.register(ProjectIndividual)

class ProjectProductInline(admin.TabularInline):
    model = get_model('projects', 'projectproduct')   
    form = ProjectProductsAdminModelForm
    extra = 1
    
databrowse.site.register(ProjectProduct)
    
class ProjectImageInline(ImageInline):
    exclude = ('feature', 'slide_show')
    model = get_model('images', 'projectimage')
    
databrowse.site.register(ProjectImage)
    
    
class ProjectAdmin(BaseAdmin):
    list_display = (
        'title',
        'created_meta',
        'modified_meta',
        'publishing_meta',
        'is_published',
    )
    
    list_editable = (
        # 'is_published',
    )
    
    # filter_horizontal = ('project_categories', 'project_types')
    
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'summary',
                'content',
            )
        }),
        ('Publishing', {
            'fields': (
                # 'feature', 
                'sites',
                )
        }),
        ('Project Information', {
            # 'classes': ('collapse',),
            'fields': (
                'project_categories', 
                'project_types',
                'project_status',
                'project_website',
                'client',
                'client_website',
                'client_website_name',
                'number_of_stories',
                'site_type',
                'site_size',
                'building_area',
                'budget_total',
                'design_documentation',
                'construction',
                )
        }),
        ('Project Location', {
            # 'classes': ('collapse',),
            'fields': (
                'street', 
                'city', 
                'suburb',
                'country',
                'state',
                'post_code',
                )
        }),
        ('Meta', {
            'classes': ('collapse',),
            'fields': (
                'is_published',
                'published',
                # 'slug',
                'tags',
                )
        }),
    )
    
    filter_horizontal = ('tags',)
    
    inlines = [
        ProjectCompanyInline,
        ProjectIndividualInline,
        ProjectProductInline,
        ProjectImageInline,
        # ProjectDetailInline,
    ]
    
    form = ProjectAdminModelForm

admin.site.register(get_model('projects', 'project'), ProjectAdmin)
databrowse.site.register(Project)
