from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r"^login/$", 
        "base.views.login",
        name="base_acct_login"),
    url(r"^comment-login/$", 
        "base.views.login",
        name="base_comment_acct_login"),
)