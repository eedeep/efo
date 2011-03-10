from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from features.models import Feature, FeatureSet, SiteFeatureArea
from features.utils import get_features
from articles.models import Article


import datetime


def home(request): 
    
    """
    Show feature objects
    
    """
    
    # Home Features
    home_features = get_features('home')
    
    # Editors Choice
    editors_choices = get_features('editors_choice')[:3]
    
    # All features
    all_features = home_features + editors_choices
    
    """
    Get latest 'feature articles' where they are not in the current features areas, or editors choices
    """
    
    # Get the article content type
    article_ctype = ContentType.objects.get_for_model(Article)
    featured_articles = [feature.content_object for feature in all_features if feature.content_type == article_ctype]
    
    article_kwargs = {
        'is_published': True,
        'published__lte': datetime.datetime.now(),
        'article_type__is_published': True, }
        
    latest_articles = Article.site_objects \
        .filter(**article_kwargs) \
        .exclude(pk__in=[article.id for article in featured_articles]) \
        .order_by("-published")
    
    return render_to_response(
        'homepage.html',
        {
            "home_features": home_features,
            "latest_articles": latest_articles,
        },
        context_instance=RequestContext(request))
        
