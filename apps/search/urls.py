from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$',
        'search.views.search',   
        name="search_query",
    ),
)

# ?q=(?P<q>.*)$',