# django imports
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson

from projects.models import ProjectIndividual
from articles.models import Article

from django.contrib.comments.models import Comment

import datetime

def search(request, q=""):
    """
    """
    q = request.GET.get("q", "")
    
    results = []
    total = 0
    
    article_kwargs = {
        'is_published': True,
        'published__lte': datetime.datetime.now(),
        'article_type__is_published': True,
    }
    
    if q == "":
        # Nothing to search for.
        pass
    else:
        # Articles
        query = Q(is_published=True) & \
                Q(title__icontains=q) | \
                Q(content__icontains=q)
        
        articles = Article.site_objects.filter(query, **article_kwargs)
        
        results = articles
        
        # total = len(results)
        
        # # Events
        #         
        #         # Projects
        #         
        #         # Organisations
        #         query = Q(active=True) & \
        #                 Q(name__icontains=q) | \
        #                 Q(variants__name__icontains=q)
        #                 #Q(manufacturer__name__icontains=q) | \
        # 
        #         temp = Product.objects.filter(query).select_related() # Get variants via select_related?
        #         total = len(temp)
        #         products = temp[0:5]

    return render_to_response(
        'search/results.html',
        {
            "results": results,
            "q": q,
            "total": total
        },
        context_instance=RequestContext(request))