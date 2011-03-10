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
    ImagesProjectimage, \
    ImagesImage, \
    PublicationsMagazineissue, \
    TaggitTag, \
    ProjectsProjectstatus, \
    ProjectsProject, \
    ProjectsProjectcategory, \
    ProjectsProjectcompany, \
    ProjectsProjectdetail, \
    ProjectsProjectindividual, \
    ProjectsProjectproduct, \
    ProjectsProjectProjectCategories, \
    ProjectsProjectProjectTypes, \
    ProjectsProjectrole, \
    ProjectsProjectSites, \
    ProjectsProjectsitetype, \
    ProjectsProjectTags, \
    ProjectsProjecttype, \
    OrganisationsOrganisation, \
    OrganisationsOrganisationexpertise, \
    OrganisationsOrganisationOrganisationExpertise, \
    OrganisationsOrganisationOrganisationType, \
    OrganisationsOrganisationSites, \
    OrganisationsOrganisationTags, \
    OrganisationsOrganisationtype

from meta.utils import SlugifyUniquely
from projects.models import Project, ProjectProduct, ProjectIndividual, ProjectRoleType, ProjectCompany

from imagess.models import ArticleImage as OldArticleImage
from imagess.models import ProjectImage as OldProjectImage

from images.models import ArticleImage
from taggit.models import Tag
from organisations.models import Organisation
from colophon.models import Publisher

import datetime, os.path

class Command(BaseCommand):
    help = 'migrate projects'

    def handle(self, *args, **options):
        """
        Projects
        """
        
        articles_to_link = []
        projects_to_link = []
        unlinked_projects = []
        
        publisher = Publisher.objects.get(pk=1)
        user = User.objects.get(pk=1)
        
        l_projects = ProjectsProject.objects.all()        
    
        for l_project in l_projects:
            
            # Get related data
            sites = Site.objects.filter(pk=1)
            
            ProjectsProjectProjectCategories
            categories = ProjectsProjectcategory.objects.filter(projectsprojectprojectcategories__project_id=l_project.id)
            types = ProjectsProjecttype.objects.filter(projectsprojectprojecttypes__project_id=l_project.id)
            
            try:
                status = ProjectsProjectstatus.objects.get(projectsproject__id=l_project.id)
            except:
                status = None
            
            # print u''
            #             print u'===================================='
            #             print u''
            print u'%s' % l_project.title
            # print u''
            #             print u'::: Categories: %s ::: Types: %s ::: Status: %s' % (categories.values_list(flat=True), types.values_list(flat=True), status)
            
            
            # ============================
            # List & Create new records
            
            #### Organisations
            
            
            
            #### Projects
            
            p_kwargs = {
                'title': l_project.title,
                'building_area': l_project.building_area,
                'budget_total': l_project.budget_total,
                'city': l_project.city,
                'client': l_project.client,
                'client_website': l_project.client_website,
                'client_website_name': l_project.client_website_name,
                'construction': l_project.construction,
                'content': l_project.content,
                'country': l_project.country,
                'created': datetime.datetime.now(),
                'created_by': user,
                'design_documentation': l_project.design_documentation,
                'old_id': l_project.id,
                'is_published': True,
                'number_of_stories': l_project.number_of_stories,
                'post_code': l_project.post_code,
                'project_website': l_project.client_website,
                'published': datetime.datetime.now(),
                'published_by': user,
                'publisher': publisher,
                'short_title': l_project.title,
                'site_size': l_project.site_size,
                'slug': SlugifyUniquely(truncate_words(l_project.title, 4), Project),
                'state': l_project.state,
                'street': l_project.street,
                'suburb': l_project.suburb,
                'summary': l_project.summary
            }
            project = Project(**p_kwargs)
            
            if status:
                try:
                    project.project_status = ProjectStatus.objects.get(pk=1)
                except:
                    pass
                
            try:
                project = Project.objects.get(title=project.title)
            except ObjectDoesNotExist:
                # Create new
                try:
                    project.full_clean()
                    # pass
                except ValidationError, e:
                    # Do something based on the errors contained in e.message_dict.
                    # Display them to a user, or handle them programatically.
                    print e
                else:
                    # Save new
                    # project.save()
                    # if project.save():
                    # project.organisation_type = l_org_types
                    project.save()
                    print u'=== === === saving project %s' % project
            else:
                # Once saved, add related items == 
                print u'=== === === project exists %s' % project
                # Clean up or add
            
                # Products
                l_p_products = ProjectsProjectproduct.objects.filter(project=l_project)
                for l_p_product in l_p_products:
                    print u'--- --- %s :: %s' % (l_p_product.label, l_p_product.products)
                    pp_kwargs = {
                        'project': project,
                        'label': l_p_product.label,
                        'products': l_p_product.products
                    }
                    project_product = ProjectProduct(**pp_kwargs)
                    try:
                        project_product.full_clean()
                        # pass
                    except ValidationError, e:
                        # Do something based on the errors contained in e.message_dict.
                        # Display them to a user, or handle them programatically.
                        print e
                    else:
                        try:
                            pp = ProjectProduct.objects.get(label=l_p_product.label, project=l_project)
                        except MultipleObjectsReturned:
                            pps = ProjectProduct.objects.filter(label=l_p_product.label, project=l_project)[2:]
                            ipdb.set_trace()
                            for pp in pps:
                                pp.delete()
                                print u'=== === === deleting products :: %s' % pp
                        except ObjectDoesNotExist:
                            project_product.save()
                            print u'=== === === saving new products :: %s' % project_product
                        else:
                            print u'=== === === products already exists :: %s' % project_product

                        
                
                ##### Project Roles
                
                # Individuals
                l_p_individuals = ProjectsProjectindividual.objects.filter(project=l_project)
                # l_p_individuals = [] # prevents from processing
                for l_p_individual in l_p_individuals:
                    
                    try:
                        organisation = Organisation.objects.get(title=l_p_individual.organisation.title)
                    except ObjectDoesNotExist:
                        """
                        Does not exist, so create new.
                        """
                        o_kwargs = {
                            'title': l_p_individual.organisation.title,
                            'content': l_p_individual.organisation.content,
                            'street': l_p_individual.organisation.street,
                            'suburb': l_p_individual.organisation.suburb,
                            'city': l_p_individual.organisation.city,
                            'country': l_p_individual.organisation.country,
                            'state': l_p_individual.organisation.state,
                            'post_code': l_p_individual.organisation.post_code,
                            'phone': l_p_individual.organisation.phone,
                            'fax': l_p_individual.organisation.fax,
                            'mobile': l_p_individual.organisation.mobile,
                            'email': l_p_individual.organisation.email,
                            'website': l_p_individual.organisation.website,
                            'website_name': l_p_individual.organisation.website_name,
                        }
                    
                        organisation = Organisation(**o_kwargs)
                        print u'=== === saving %s' % organisation
                        try:
                            organisation.full_clean()
                        except ValidationError, e:
                            # Do something based on the errors contained in e.message_dict.
                            # Display them to a user, or handle them programatically.
                            print e
                        else:
                            organisation.save()
                            print u'=== === === saving %s' % organisation
                    
                    p_individual = {
                        'project': project,
                        # 'role': role_type,
                        # 'individual': None,
                        'credit': l_p_individual.credit,
                        'custom_credit': l_p_individual.role,
                        'organisation': organisation,
                    }
                    project_individual = ProjectIndividual(**p_individual)
                    try:
                        project_individual.full_clean()
                    except ValidationError, e:
                        # Do something based on the errors contained in e.message_dict.
                        # Display them to a user, or handle them programatically.
                        print e
                    else:
                        try:
                            pi = ProjectIndividual.objects.get(custom_credit=l_p_individual.role)
                        except MultipleObjectsReturned:
                            pi = ProjectIndividual.objects.filter(custom_credit=l_p_individual.role)[0]
                            pi.delete()
                            print u'=== === === deleting :: %s' % pi
                        except ObjectDoesNotExist:
                            project_individual.save()
                            print u'=== === === saving new :: %s' % project_individual
                        else:
                            print u'=== === === already exists :: %s' % project_individual
                
                
                l_p_companies = ProjectsProjectcompany.objects.filter(project=l_project)
                # l_p_companies = []
                for l_company in l_p_companies:
                    print u'=== %s' % l_company.organisation.title
                
                    # Get Organisation Type
                    l_org_types = OrganisationsOrganisationtype.objects.filter(organisationsorganisationorganisationtype__organisation_id=l_company.organisation.id)
                
                    try:
                        organisation = Organisation.objects.get(title=l_company.organisation.title)
                    except ObjectDoesNotExist:
                        """
                        Does not exist, so create new.
                        """
                        o_kwargs = {
                            'title': l_company.organisation.title,
                            'content': l_company.organisation.content,
                            'street': l_company.organisation.street,
                            'suburb': l_company.organisation.suburb,
                            'city': l_company.organisation.city,
                            'country': l_company.organisation.country,
                            'state': l_company.organisation.state,
                            'post_code': l_company.organisation.post_code,
                            'phone': l_company.organisation.phone,
                            'fax': l_company.organisation.fax,
                            'mobile': l_company.organisation.mobile,
                            'email': l_company.organisation.email,
                            'website': l_company.organisation.website,
                            'website_name': l_company.organisation.website_name,
                        }
                    
                        organisation = Organisation(**o_kwargs)
    
                        try:
                            organisation.full_clean()
                        except ValidationError, e:
                            # Do something based on the errors contained in e.message_dict.
                            # Display them to a user, or handle them programatically.
                            print e
                        else:
                            # pass
                            # organisation.save()
                            if organisation.save():
                                organisation.organisation_type = l_org_types
                            print u'=== === === saving %s' % organisation
                    else:
                        
                        # Organisation does exist, so do any cleanups.
                        print u'=== === === exists :: cleaning %s' % organisation
                        if l_company.organisation.logo_image:
                           organisation.logo_image = os.path.join("files", "logos", os.path.basename(l_company.organisation.logo_image))
                        else:
                           organisation.logo_image = None
                           organisation.save()
                
                
                    try:
                        role_type = ProjectRoleType.objects.get(name=l_company.role)
                    except ObjectDoesNotExist:
                        # Create new role
                        rt_kwargs = {
                            'name': l_company.role,
                            'slug': SlugifyUniquely(truncate_words(l_company.role, 4), ProjectRoleType),
                        }
                        role_type = ProjectRoleType(**rt_kwargs)
                        try:
                            role_type.full_clean()
                        except ValidationError, e:
                            # Do something based on the errors contained in e.message_dict.
                            # Display them to a user, or handle them programatically.
                            print e
                        else:
                            role_type.save()
                
                    p_company = {
                        'project': project,
                        'role': role_type,
                        # 'individual': None,
                        'credit': l_company.credit,
                        'organisation': organisation,
                    }
                    project_company = ProjectCompany(**p_company)
                    try:
                        project_company.full_clean()
                    except ValidationError, e:
                        # Do something based on the errors contained in e.message_dict.
                        # Display them to a user, or handle them programatically.
                        print e
                    else:
                        try:
                            pc = ProjectCompany.objects.get(organisation=organisation, role=role_type)
                        except MultipleObjectsReturned:
                            pc = ProjectCompany.objects.filter(organisation=organisation, role=role_type)[0]
                            pi.delete()
                            print u'=== === === deleting :: %s' % pc
                            # pass
                        except ObjectDoesNotExist:
                            project_company.save()
                            print u'=== === === saving new :: %s' % project_company
                            # pass
                        else:
                            print u'=== === === already exists :: %s' % project_company
                            # pass
                
                
                # re-attach article relation.
                
                # Get old relation
                try:
                    l_article = ArticlesArticle.objects.get(project=l_project)
                except ObjectDoesNotExist:
                    unlinked_projects.append(l_project)
                except MultipleObjectsReturned:
                    # wtf?
                    print "**** multiple articles linking to the same project found"
                    # ipdb.set_trace()
                    pass
                else:
                    try:
                        article = Article.objects.get(title=l_article.title)
                    except ObjectDoesNotExist:
                        # Couldn't match on title so make a note for manual linking
                        articles_to_link.append(article)
                    else:
                        try:
                            article.project = Project.objects.get(title=l_project.title)
                        except ObjectDoesNotExist:
                            # Couldn't get a match on project... should do this manually
                            projects_to_link.append(l_project)
                        else:
                            print u'*** saving %s ::: to ::: %s' % (article.project, article)
                            article.save()
                
                project.save()
                
        # ipdb.set_trace()
            # print u'===================================='