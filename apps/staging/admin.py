from django.contrib import admin
from django.contrib.sites.models import Site
from django.db.models import get_model
from django.shortcuts import _get_queryset

# class ArticlesArticle(models.Model):
# 
# 
# class ArticlesArticlesection(models.Model):
# 
# 
# class ArticlesArticlesectionimage(models.Model):
# 
# 
# class PublicationsMagazine(models.Model):
# 
# 
# class PublicationsMagazineissue(models.Model):

class ArticlesArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(get_model('staging', 'articlesarticle'), ArticlesArticleAdmin)
admin.site.register(get_model('staging', 'articlesarticlesection'))
admin.site.register(get_model('staging', 'articlesarticlesectionimage'))
admin.site.register(get_model('staging', 'publicationsmagazine'))
admin.site.register(get_model('staging', 'publicationsmagazineissue'))