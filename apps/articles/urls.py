from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'articles.views.articles',
        name="articles_articles"
    ),
    url(
        r'^article/(?P<slug>.*)$',
        'articles.views.article',   
        name="article_view",
    ),
    url(
        r'^types/(?P<article_type>.*)/(?P<tag>.*)$',
        'articles.views.articles',
        name="articles_article_type_tag"
    ),
    url(
        r'^types/(?P<article_type>.*)$', 
        'articles.views.articles',
        name="articles_article_type"
    ),
    
    # Deprecate below
    url(
        r'^sections/(?P<article_type_section>.*)$', 
        'articles.views.articles',
        name="articles_section"
    ),
    url(
        r'^(?P<article_type_section>\w+)/(?P<article_type>.*)$', 
        'articles.views.articles',
        name="articles_section_type"
    ),
)