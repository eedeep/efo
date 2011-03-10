from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.http import base36_to_int
from django.utils.translation import ugettext, ugettext_lazy as _

from emailconfirmation.models import EmailAddress, EmailConfirmation

association_model = models.get_model("django_openid", "Association")
if association_model is not None:
    from django_openid.models import UserOpenidAssociation

from pinax.apps.account.utils import get_default_redirect, user_display
from pinax.apps.account.models import OtherServiceInfo
from pinax.apps.account.forms import AddEmailForm, ChangeLanguageForm, ChangePasswordForm
from pinax.apps.account.forms import ChangeTimezoneForm, LoginForm, ResetPasswordKeyForm
from pinax.apps.account.forms import ResetPasswordForm, SetPasswordForm, SignupForm
from pinax.apps.account.forms import TwitterForm

def group_and_bridge(kwargs):
    """
    Given kwargs from the view (with view specific keys popped) pull out the
    bridge and fetch group from database.
    """
    
    bridge = kwargs.pop("bridge", None)
    
    if bridge:
        try:
            group = bridge.get_group(**kwargs)
        except ObjectDoesNotExist:
            raise Http404
    else:
        group = None
    
    return group, bridge


def group_context(group, bridge):
    # @@@ use bridge
    return {
        "group": group,
    }
    
def login(request, **kwargs):
    
    form_class = kwargs.pop("form_class", LoginForm)
    template_name = kwargs.pop("template_name", "account/login.html")
    
    associate_openid = kwargs.pop("associate_openid", False)
    openid_success_url = kwargs.pop("openid_success_url", None)
    url_required = kwargs.pop("url_required", False)
    extra_context = kwargs.pop("extra_context", {})
    redirect_field_name = kwargs.pop("redirect_field_name", "next")
    
    if request.POST["success_url"]:
        success_url = request.POST["success_url"]
    else:
        success_url = kwargs.pop("success_url", None)
    
    group, bridge = group_and_bridge(kwargs)
    
    if extra_context is None:
        extra_context = {}
    if success_url is None:
        success_url = get_default_redirect(request, redirect_field_name)
    
    if request.method == "POST" and not url_required:
        form = form_class(request.POST, group=group)
        if form.is_valid():
            form.login(request)
            if associate_openid and association_model is not None:
                for openid in request.session.get("openids", []):
                    assoc, created = UserOpenidAssociation.objects.get_or_create(
                        user=form.user, openid=openid.openid
                    )
                success_url = openid_success_url or success_url
            messages.add_message(request, messages.SUCCESS,
                ugettext(u"Successfully logged in as %(user)s.") % {
                    "user": user_display(form.user)
                }
            )
            return HttpResponseRedirect(success_url)
    else:
        form = form_class(group=group)
    
    ctx = group_context(group, bridge)
    
    ctx.update({
        "form": form,
        "url_required": url_required,
        "redirect_field_name": redirect_field_name,
        "redirect_field_value": request.REQUEST.get(redirect_field_name),
    })
    ctx.update(extra_context)
    
    return render_to_response(template_name, RequestContext(request, ctx))
    
def logout(request, next_page=None, template_name='registration/logged_out.html', redirect_field_name=REDIRECT_FIELD_NAME):
    "Logs out the user and displays 'You are logged out' message."
    from django.contrib.auth import logout
    logout(request)
    messages.add_message(request, messages.SUCCESS,
        ugettext(u"Successfully logged out!"))
    if next_page is None:
        redirect_to = request.REQUEST.get(redirect_field_name, '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(template_name, {
                'title': _('Logged out')
            }, context_instance=RequestContext(request))
    else:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page or request.path)