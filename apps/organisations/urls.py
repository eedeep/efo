from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'organisations.views.organisations',
        name="organisations_organisations"
    ),
    url(
        r'^(?P<slug>.*)$',
        'organisations.views.organisation',   
        name="organisation_view",
    ),
    
)