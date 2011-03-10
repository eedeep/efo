# from django.contrib import admin
# from django.db.models import get_model
# from django.contrib.sites.models import Site 
# 
# class RegionAdmin(admin.ModelAdmin):
#     
#     list_display = (
#         'site',
#         'country_code',
#         'default',
#     )
#     
#     list_editable = (
#         'country_code',
#         'default',
#     )
#     
# admin.site.register(get_model('regions', 'region'), RegionAdmin)