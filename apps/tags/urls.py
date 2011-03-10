from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'tags.views.index',
        name="tags_index"
    ),
    url(
        r'^(?P<tag_slug>.*)$',
        'tags.views.tag',   
        name="tag_view",
    ),
)