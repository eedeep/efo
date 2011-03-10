from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^subscribe/$', 
        'inbox.views.subscribe',
        name="inbox_subscribe"
    ),
    url(
        r'^success/$',
        'inbox.views.success',
        name="inbox_success",
    ),
)