from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Count

from publications.models import Magazine, MagazineIssue
from articles.models import Article
from archive.models import ArchiveArticle
        
def magazine(request, magazine_slug=None, filter_by_year=None):
    
    magazine = get_object_or_404(Magazine, slug=magazine_slug)
    
    issue_kwargs = {
        'issue__magazine': magazine }
    
    # Get the articles & archive articles
    archive_articles = ArchiveArticle.objects.filter(**issue_kwargs)
    articles = Article.objects.filter(issues__magazine=magazine)
    
    # Get only the years that have magazine issues and articles
    available_years = list(archive_articles.values_list('issue__issue_year', flat=True))
    for article in articles:
        try:
            [available_years.append(issue_year) for issue_year in article.issues.all().values_list('issue_year', flat=True)]
        except:
            pass
    
    available_years = [available_year for available_year in set(available_years)]
    available_years.sort(reverse=True)
    
    if filter_by_year:
        issue_kwargs.update({
            'issue__issue_year': filter_by_year, })
    # Get only the issues that have related articles
    articles = archive_articles.filter(**issue_kwargs).only('issue').order_by('-issue__issue_year')
    
    issues = [article.issue for article in articles]
    issues = [issue for issue in set(issues)]
    issues.sort(key=lambda issue:issue.issue_year, reverse=True)
    
    # Perhaps the available years should come from here, saving a few queries?
    # TODO: get also issues with relationships to new articles
    
    return render_to_response(
        'publications/magazine.html',
        {
            "magazine": magazine,
            "issues": issues,
            "available_years": available_years,
            "filter_by_year": filter_by_year,
        },
        context_instance=RequestContext(request))

def magazine_issue(request, magazine_slug, issue_slug):

    issue = get_object_or_404(MagazineIssue, slug=issue_slug)

    """
    At the moment we are just order the sections by whatever order they were initially inserted 
    into the database in. In the future it may be necessary to provide an explicit order field
    that controls what order the sections appear in on the TOC page. Within a section we
    are currently ordering by page_number.
    """
    if issue.is_from_the_archive():
        articles = issue.archivearticle_set.all().order_by('-magazine_section__id', 'page_number') 
    else:
        articles = issue.article_set.all().order_by('-magazine_section__id', 'page_number')

    return render_to_response(
        'publications/magazine_issue.html',
        {
            "issue": issue,
            "articles": articles,
        },
        context_instance=RequestContext(request))
