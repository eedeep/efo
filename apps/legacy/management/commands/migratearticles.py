from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import truncate_words

from articles.models import Article, ArticleType
from colophon.models import Publisher

from legacy.models import \
    ArticlesArticle, \
    ArticlesArticleTags, \
    ArticlesArticletype, \
    ImagesArticleimage, \
    ImagesImage, \
    PublicationsMagazineissue, \
    TaggitTag

from meta.utils import SlugifyUniquely
from projects.models import Project
from imagess.models import ArticleImage as OldArticleImage
from publications.models import MagazineIssue
from images.models import ArticleImage
from taggit.models import Tag

# class ImagesImage(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=200)
#     slug = models.CharField(max_length=50)
#     caption = models.TextField()
#     image = models.CharField(max_length=100)
#     feature = models.BooleanField()
#     slide_show = models.BooleanField()
#     class Meta:
#         db_table = u'images_image'
# 
# class ImagesArticleimage(models.Model):
#     image_ptr = models.ForeignKey(ImagesImage)
#     article = models.ForeignKey(ArticlesArticle)
#     class Meta:
#         db_table = u'images_articleimage'

class Command(BaseCommand):
    help = 'migrate articles'

    def handle(self, *args, **options):
        """
        Articles
        """
    
        l_articles = ArticlesArticle.objects.all()
    
        user = User.objects.get(pk=1)
    
        for l_article in l_articles:
        
            """
            Relationships
            
                Project, Publisher, Publication, ArticleType, Users(Authors)
            """
            
            # try:
            #              # project = Project.objects.get(l_)
            #          except:
            project = None
                
            try:
                publisher = Publisher.objects.get(pk=1)
            except:
                publisher = None
        
            try:
                article_type = ArticleType.objects.get(pk=l_article.article_type.id)
            except:
                article_type = ArticleType.objects.get(pk=1)
            
            l_magazines = PublicationsMagazineissue.objects.filter(articlesarticlemagazines=l_article) 
            
            magazines = MagazineIssue.objects.filter(id__in=[l_magazine.id for l_magazine in l_magazines])
            
            # Tags
            l_article_tags = ArticlesArticleTags.objects.filter(article_id=l_article.id)
            tags = TaggitTag.objects.filter(id__in=l_article_tags.values_list('tag_id'))
            
            # Images
            #        images = []
            #        
            #        import ipdb; ipdb.set_trace()
            #        
            # images = ArticleImage.objects.filter()
    

            sites = Site.objects.filter(pk=1)
            users = User.objects.filter(pk=1)
           

            kwargs = {
                'article_type': article_type,
                'content':  l_article.content,
                'created': l_article.created,
                'created_by': user,
                'introduction': l_article.summary,
                'is_published': l_article.is_published,
                # 'old_id': l_article.id,
                'project': project,
                'published': l_article.published,
                'published_by': user,
                'publisher': publisher,
                'short_title': l_article.title, # Truncated?
                'slug': SlugifyUniquely(truncate_words(l_article.title, 4), Article),
                'summary': l_article.summary,
                'title': l_article.title,
                # 'articles_article_authors': users,
                # 'magazines': magazines,
                # 'tags': tags
                 }
            
            article = Article(**kwargs)
            
            try:
                article.full_clean()
                # pass
            except ValidationError, e:
                # Do something based on the errors contained in e.message_dict.
                # Display them to a user, or handle them programatically.
                print e
            else:
                try:
                    article = Article.objects.get(title=article.title)
                except ObjectDoesNotExist:
                    """
                    Does not exist, so create new.
                    """
                    print u'=== saving %s' % article
                    if article.save():
                        article.users = users
                        article.magazines = magazines
                        article.tags = tags
                        print u'====== saving m2m %s' % article
                        # article.save()
                else:
                    """
                    Already exists, do other cleanups if necessary
                    """
                    print u'+++ duplicate %s' % article
                    # article.magazines = magazines
                    # article.old_id = l_article.id
                    article.slug = SlugifyUniquely(truncate_words(article.title, 3), Article)
                    print u'+++ slug %s' % len(article.slug)
                    
                    if len(article.slug) > 40:
                        print u'+++ slug too long for %s' % article.slug
                    
                    # Images here.
                    
                    l_images = OldArticleImage.objects.filter(article__id=article.id)
                    
                    for l_image in l_images:
                        
                        ai_kwargs = {
                            'article_id':article.id,
                            'image': u'files/%s' % (l_image.image),
                            'caption': l_image.caption,
                            'slug': SlugifyUniquely(truncate_words(l_image.title, 4), ArticleImage),
                            'user_credit': user,
                        }
                        
                        article_image = ArticleImage(**ai_kwargs)
                        
                        try:
                            article_image.full_clean()
                            # pass
                        except ValidationError, e:
                            # Do something based on the errors contained in e.message_dict.
                            # Display them to a user, or handle them programatically.
                            print u'******** %s ********' % e
                        else:
                            try:
                                ArticleImage.objects.get(image=article_image.image)
                            except ObjectDoesNotExist:
                                # Doesn't exist, save
                                print u':: Saving %s' % article_image
                                # article_image.save()
                            except MultipleObjectsReturned:
                                # Duplicates, need to prune
                                print u':: Multiple images here!'
                                article_images = ArticleImage.objects.filter(image=article_image.image)
                                i = 0
                                for article_image in article_images:
                                    if i > 0:
                                        # article_image.delete()
                                        print u'***** deleting :: %s' % article_image
                                    i += 1
                            else:
                                # One object. Do nothing
                                pass
                                
                    # Clean current blank images
                    for image in ArticleImage.objects.filter(article__id=article.id):
                        # print u':: Image :: %s' % image
                        if not image.image:
                            print u'============== Image missing! Delete :: %s' % image
                            # image.delete()
                                
                        # print u'%s::%s::%s' % (article, article_image, l_image.article)
                    try:
                        article.full_clean()
                        # pass
                    except ValidationError, e:
                        # Do something based on the errors contained in e.message_dict.
                        # Display them to a user, or handle them programatically.
                        print e
                    else:
                        # print u':: Saving %s' % article
                        article.save()
                
                # print users
                # print u'ids :: %s :: %s' % (article.id, article.old_id)
                # print u'slug :: %s :: %s' % (article, article.slug)
                # print u'%s :: %s' % (l_magazines.values_list(), magazines.values_list())
                # print sites
                # print u'images :: %s :: %s' % (l_images.values_list(), images)
                # print u'%s :: %s' % (l_article_tags.values_list('tag_id'), tags.values_list('id'))