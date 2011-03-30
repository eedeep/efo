from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^programme/(?P<slug>.*)$',
        'programmes.views.programme',   
        name="programme_view",
    ),
    url(
        r'^$', 
        'programmes.views.programmes',
        name="programmes_programmes"
    ),
)
