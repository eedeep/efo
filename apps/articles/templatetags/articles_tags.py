from articles.models import Article, ArticleType
from django import template
from django.contrib.sites.models import Site
from django.template import Context
from django.template.loader import get_template

from taggit.models import Tag
import datetime


register = template.Library()

@register.inclusion_tag('base/_asides_object_list.html')
def latest_news():
    articles = Article.site_objects.filter(is_published=True, article_type__section='news').order_by('-published')[0:3]
    return { 
        'objects': articles,
    }
    
@register.inclusion_tag('articles/_article_type_nav_list.html')
def article_type_nav_list():
    article_type_kwargs = {
        'is_published': True,
        'is_navigable': True,}
    
    article_types = ArticleType.objects.filter(**article_type_kwargs)
    active_article_type_list = []
    
    article_kwargs = {
        'is_published': True,
        'published__lte': datetime.datetime.now(),
        'sites': Site.objects.get_current().id,}
    
    for article_type in article_types:
        if len(article_type.article_set.filter(**article_kwargs)):
            active_article_type_list.append(article_type)
    
    return { "article_types": active_article_type_list }
    
@register.inclusion_tag('articles/_article_type_tags_nav_list.html')
def article_type_tags_nav_list(article_type, current_tag=None):

    article_type_tags_kwargs = {
        'articletype__is_published': True,
        'articletype__is_navigable': True,
        'articletype': article_type, }
    
    tags = Tag.objects.filter(**article_type_tags_kwargs)
    
    article_kwargs = {
        'is_published': True,
        'published__lte': datetime.datetime.now(),
        'article_type': article_type, }
    
    article_type_tags = []
    
    for tag in tags:
        tag.current_article_type = article_type
        article_kwargs.update({
            'tags': tag,
        })
        if Article.objects.filter(**article_kwargs).count():
            article_type_tags.append(tag)
            
    context = { "article_type_tags": article_type_tags }
    
    if current_tag:
        context.update({
            "current_tag": current_tag,
        })
    
    return context

@register.filter
def render_inline_images_for(html, article):
    """
    Filter that accepts a string of HTML, typically from a TinyMCE controlled 
    field, and searchs the HTML for images that match the list of inline 
    images on the given article object. For any matches found, replace the 
    image tag with the rendered template "articles/_inline_image.html" which 
    contains a single variable "inline_image" - within this template it is 
    now possible to access the caption and credits for the image.
    """
    token = "%placeholder%"
    for image in article.articleimage_set.all():
        try:
            """
            @Stephen
            
                1.  This needs to change to match a subset of the image,
                    such that filebrowser 'versions' will work
                2.  This seems to spitting out an extra '>', &
                3.  if width & height is specified on the image attributes,
                    those need to flow through to the template
            """
            url = image.image.url_relative
        except AttributeError:
            continue
        while url in html:
            start = html.rfind("<", 0, html.find(url))
            end = html.find(">", html.find(url)) + 1
            html = html[:start] + token + html[end:]
            image.inline_width = 300
            image.inline_height = 200
            
        t = get_template("articles/_inline_image.html")
        rendered = t.render(Context({"inline_image": image}))
        html = html.replace(token, rendered)
        
    return html
