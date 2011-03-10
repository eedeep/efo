from django.contrib import admin
from django.db.models import get_model

# class TopicInline(admin.TabularInline):
#     model = get_model('topics', 'topic')   
# 
# class TopicalContentAdmin(admin.ModelAdmin):
#     # inlines = [
#     #         TopicInline,
#     #     ]
#     pass
#     
# admin.site.register(get_model('topics', 'topicalcontent'), TopicalContentAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
        'active',
    )
    
    list_editable = (
        'active',
    )

admin.site.register(get_model('topics', 'topic'), TopicAdmin)

