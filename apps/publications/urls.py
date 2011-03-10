from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^(?P<magazine_slug>.*)/(?P<issue_year>\d{4})/(?P<issue_slug>.*)/(?P<article_slug>.*)$',
        'archive.views.archive_article', 
        name="archive_article_view",
    ),
    url(
        r'^(?P<magazine_slug>.*)/(?P<filter_by_year>\d{4})/$',
        'publications.views.magazine',   
        name="magazine_view_by_year",
    ),
    url(
        r'^(?P<magazine_slug>.*)/(?P<issue_slug>.*)/$',
        'publications.views.magazine_issue',
        name="magazine_issue_view",
    ),
    url(
        r'^(?P<magazine_slug>.*)/$',
        'publications.views.magazine',   
        name="magazine_view",
    )
)
