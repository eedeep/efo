from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext
from filebrowser.functions import handle_file_upload

import settings, os.path

from articles.models import Article
from profiles.models import Profile
from projects.models import ProjectIndividual

from profiles.forms import ProfileAccountForm, ContributorAccountForm

def index(request):
    
    profiles = get_list_or_404(Profile)
    
    return render_to_response(
        'profiles/index.html',
        {
            "profiles": profiles,
        },
        context_instance=RequestContext(request))
        
def profile(request, profile_id=None, username=None):
    
    profile = get_object_or_404(Profile, user__username=username)
    comments = Comment.objects.filter(
        user__username=username,
        is_removed=False)
    articles = Article.objects.filter(
        users__username=username,
        is_published=True)
    project_roles = ProjectIndividual.objects.filter(individual__username=username)
    
    # Put the following in a reusable 'objects_stream():'
    # stream_objects = []
    # 
    # for comment in comments.all():
    #     stream_object = comment
    #     stream_object.stream_date = comment.submit_date
    #     stream_objects.append(stream_object)
    #     
    # for article in articles.all():
    #     stream_object = article
    #     stream_object.stream_date = article.published
    #     stream_objects.append(stream_object)
    #     
    # # for project_role in project_roles.all():
    # #        stream_object = project_role
    # #        stream_object.stream_date = project_role.project.published
    # #        stream_objects.append(stream_object) 
    # 
    # stream_objects.sort(key=lambda obj:obj.stream_date, reverse=True)
    
    return render_to_response(
        'profiles/profile.html',
        {
            "profile": profile,
            "comments": comments,
            "articles": articles,
            # "stream_objects": stream_objects,   
        },
        context_instance=RequestContext(request))

@login_required      
def account(request, form_class=ProfileAccountForm):
    """
    Update a profiles account as a Contributor or Member in the system.
    
    Allow different account editing possibilities depending on profile_type.
    """
    
    # import ipdb; ipdb.set_trace()
    
    # Get the logged in user
    user = request.user
    
    try:
        profile = user.get_profile()
    except ObjectDoesNotExist:
        profile = None
    else:
        if profile.is_contributor:
            form_class = ContributorAccountForm
    
        if request.method == "POST":
            
            args = [request.POST,]
            if request.FILES.has_key('avatar'):
                args.append(request.FILES)
            else:
                # save the existing avatar for resave
                profile_avatar = profile.avatar
            profile_account_form = form_class(*args, instance=profile)
                
            if profile_account_form.is_valid():
                profile = profile_account_form.save(commit=False)
                profile.user = request.user # @@@ if not 'cannot edit someone elses account
                
                if profile_account_form.files.has_key('avatar'):
                    avatar_path = os.path.join(
                        settings.FILEBROWSER_MEDIA_ROOT, 
                        settings.FILEBROWSER_DIRECTORY,
                        "avatars")
                    
                    if settings.FILEBROWSER_SAVE_FULL_URL:
                        profile.avatar = os.path.join(avatar_path, request.FILES['avatar'].name)
                    else:
                        profile.avatar = os.path.join( 
                        settings.FILEBROWSER_DIRECTORY,
                        "avatars",
                        request.FILES['avatar'].name)   
                  
                    handle_file_upload(
                        avatar_path,                    
                        request.FILES['avatar'])
                # else:
                # profile.avatar = profile_avatar

                profile.save()
                messages.add_message(request, messages.SUCCESS, ugettext("Your account has been updated."))
                return HttpResponseRedirect(reverse("profile_account"))
            else:
                profile.avatar = profile_avatar # Why does this go missing?
        else:
            profile_account_form = form_class(instance=profile)
        
        return render_to_response(
            'profiles/account.html',
            {
                "profile": profile,
                "profile_account_form": profile_account_form,
            },
            context_instance=RequestContext(request))
        
def profiles(request):
    
    profiles = Profile.objects.filter(profile_type='Contributor')
    
    return render_to_response(
        'profiles/profiles.html',
        {
            "profiles": profiles,
        },
        context_instance=RequestContext(request))