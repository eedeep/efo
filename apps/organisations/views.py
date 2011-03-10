from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from base.utils import filter_by_getvalues
from popularity.signals import view

from organisations.models import Organisation
from projects.models import Project
from articles.models import Article

def index(request):
    
    organisations = filter_by_getvalues(
        request, 
        get_list_or_404(Organisation, is_published=True))
    
    return render_to_response(
        'organisations/index.html',
        {
            "organisations": organisations,
        },
        context_instance=RequestContext(request))
        
def organisation(request, organisation_id=None, slug=None):
    
    organisation = get_object_or_404(
        Organisation, 
        slug=slug, 
        is_published=True)
    
    projects = Project.objects.filter(
        projectcompany__organisation=organisation,
        is_published=True).distinct()
        
    articles = Article.objects.filter(
        project__in=projects, 
        is_published=True).distinct()
        
    location = u'%s %s' % (organisation.street, organisation.city)
        
    view.send(organisation)
    
    return render_to_response(
        'organisations/organisation.html',
        {
            "articles": articles,
            "location": location.split(),
            "organisation": organisation,
            "projects": projects,
        },
        context_instance=RequestContext(request))
        
def organisations(request):
    
    organisations = filter_by_getvalues(
        request, 
        get_list_or_404(Organisation, is_published=True)
    )
    
    return render_to_response(
        'organisations/organisations.html',
        {
            "organisations": organisations,
        },
        context_instance=RequestContext(request))