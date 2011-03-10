from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

import datetime

from articles.models import Article, ArticleType
from base.utils import filter_by_getvalues
from popularity.signals import view
from taggit.models import Tag

def article(request, article_id=None, slug=None, country_code=None):
    
    try:
        article = Article.objects.select_related().get(slug=slug, is_published=True)
    except ObjectDoesNotExist:
        raise Http404
    
    contributor_articles = Article.objects.select_related().filter(
        users__in=article.users.iterator,
        is_published=True).distinct()
    
    # tracking views with popularity
    view.send(article)
    
    return render_to_response(
        'articles/article.html',
        {
            "article": article,
            "contributor_articles": contributor_articles
        },
        context_instance=RequestContext(request))
        
def articles(request, article_type=None, tag=None):
    
    context = {}
    
    article_kwargs = {
        'is_published': True,
        'published__lte': datetime.datetime.now(),
        'article_type__is_published': True,
    }
    
    if article_type:
        article_kwargs.update({
            'article_type__slug': article_type,
        })
        try:
            article_type = ArticleType.objects.get(slug=article_type)
        except:
            pass
        else:
            context.update({
                "article_type": article_type,
            })
            
    if tag:
        try:
            tag = Tag.objects.get(slug=tag)
        except:
            pass
        else:
            article_kwargs.update({
                'tags': tag
            })
            context.update({
                'current_tag': tag,
            })
    
    # import ipdb; ipdb.set_trace()
    
    articles = Article.site_objects \
        .filter(**article_kwargs) \
        .order_by("-published")
    
    context.update({
        "articles": articles,
    })
    
    return render_to_response(
        'articles/articles.html',
        context,
        context_instance=RequestContext(request))