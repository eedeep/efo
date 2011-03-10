from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from topics.models import Topic
from articles.models import Article
from events.models import Event
from projects.models import Project
from taggit.models import Tag

def index(request):
    
    topics = get_list_or_404(Topic, active=True)
    topic_tags = [topic.tag for topic in topics]
    
    # ipdb.set_trace()
    
    return render_to_response(
        'topics/index.html',
        {
            "topic_tags": topic_tags,
        },
        context_instance=RequestContext(request))
        
def topic(request, topic_id=None, tag_slug=None):
    
    
    tag = get_object_or_404(Tag, slug=tag_slug, topic__active=True)
    
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
            tagged_objects.sort(key=lambda obj:obj.published, reverse=True)
        elif request.GET['order'] == 'discussed':
            # most discussed
            tagged_objects.sort(key=lambda obj:obj.comments_count(), reverse=True)
        elif request.GET['order'] == 'popular':
            # most popular
                tagged_objects.sort(key=lambda obj:obj.view_count(), reverse=True)
    except:
          tagged_objects.sort(key=lambda obj:obj.published, reverse=True)
    
    # ipdb.set_trace()
    
    # tagged_objects = []
    #    for tagged_item in tagged_items:
    #        if tagged_item.content_object.is_published and tagged_item.tag == tag:
    #            tagged_objects.append(tagged_item.content_object)
             
    # ipdb.set_trace()
    # tagged_items = tag.taggit_taggeditem_items.filter()
    # [tagged_item.content_object if tagged_item.content_object.is_published for tagged_item in tagged_items]
    # [tagged_item.content_object while tagged_item.content_object.is_published for tagged_item in tagged_items]
    
    return render_to_response(
        'topics/topic.html',
        {
            "topic": tag.name,
            "tagged_objects": tagged_objects,
        },
        context_instance=RequestContext(request))
        
def topics(request):
    
    topics = get_list_or_404(Topic, active=True)
    # tags = Tag.objects.filter()
    
    return render_to_response(
        'topics/topics.html',
        {
            "topics": topics,
        },
        context_instance=RequestContext(request))