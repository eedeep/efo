from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'topics.views.index',
        name="topics_index"
    ),
    url(
        r'^(?P<tag_slug>.*)$',
        'topics.views.topic',   
        name="topic_view",
    ),
)