from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^site-switch/$', 
        'colophon.views.site_switch',
        name="colophon_site_switch"
    ),
)