from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from archive.models import ArchiveArticle 
        
def archive_article(request, magazine_slug=None, issue_year=None, issue_slug=None, article_slug=None ):

    article = ArchiveArticle.objects.get(issue__slug = issue_slug, slug = article_slug)

    return render_to_response(
        'archive/article.html',
        {
            "article": article,
        },
        context_instance=RequestContext(request))
