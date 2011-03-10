from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^articles/', include('articles.urls')),
)