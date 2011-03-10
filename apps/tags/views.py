from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from taggit.models import Tag

from topics.models import Topic
from articles.models import Article
from events.models import Event
from projects.models import Project

def index(request):
    
    tags = get_list_or_404(Topic)
    
    return render_to_response(
        'tags/index.html',
        {
            "tags": tags,
        },
        context_instance=RequestContext(request))
        
def tag(request, tag_id=None, tag_slug=None):
    
    # @@@ this is copy and pasted from topics.views.topic -- some DRYing up is needed
    
    tag = get_object_or_404(Tag, slug=tag_slug)
    
    tagged_objects = []
    
    for event in Event.site_objects.filter(tags=tag, is_published=True):
        tagged_object = event
        tagged_objects.append(tagged_object)
    
    for article in Article.site_objects.filter(tags=tag, is_published=True):
        tagged_object = article
        tagged_objects.append(tagged_object)
        
    for project in Project.site_objects.filter(tags=tag, is_published=True):
        tagged_object = project
        tagged_objects.append(tagged_object)
    
    # ordering
    try:
        if request.GET['order'] == 'recent':
            # most recent
            try:
                tagged_objects.sort(key=lambda obj:obj.published, reverse=True)
            except:
                # fail silently -- @@@ should log this
                pass
        elif request.GET['order'] == 'discussed':
            # most discussed
            try:
                tagged_objects.sort(key=lambda obj:obj.comments_count(), reverse=True)
            except:
                # fail silently -- @@@ should log this
                pass
        elif request.GET['order'] == 'popular':
            # most popular
            try:
                tagged_objects.sort(key=lambda obj:obj.view_count(), reverse=True)
            except:
                # fail silently -- @@@ should log this
                pass
    except:
          tagged_objects.sort(key=lambda obj:obj.published, reverse=True)
    
    return render_to_response(
        'tags/tag.html',
        {
            "tag": tag.name,
            "tagged_objects": tagged_objects,
        },
        context_instance=RequestContext(request))
        
def tags(request):
    
    tags = get_list_or_404(Tag)
    
    return render_to_response(
        'tags/tags.html',
        {
            "tags": tags,
        },
        context_instance=RequestContext(request))