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
    
    return render_to_response(
        'homepage.html',
        {
            "home_features": home_features,
        },
        context_instance=RequestContext(request))
        
