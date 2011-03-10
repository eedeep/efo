# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from articles.models import Article
from projects.models import Project

class OldImage(models.Model):
    """
    A very simple Image model.
    
    Not 'generic' at the moment... it might be soon?
    """
    
    title = models.CharField(blank=True, max_length=200)
    slug = models.SlugField(
        blank=True,
        editable=False,
        max_length=250,
        unique=True)
        
    caption = models.TextField(blank=True)
    
    image = models.ImageField(upload_to='images')
    
    feature = models.BooleanField(
        help_text="The 'feature' image")
    slide_show = models.BooleanField(
        help_text="Include this image in a slideshow")
        
    class Meta:
        abstract=True
        db_table = u'images_image'
    
    def __unicode__(self):
        return u'%s' % (self.image)
    
class OldArticleImage(OldImage):
    article = models.ForeignKey(Article, to_field='old_id')
    image_ptr_id = models.PositiveIntegerField()
    article_id = models.PositiveIntegerField()
    class Meta:
        db_table = u'images_articleimage'
        
class OldProjectImage(OldImage):
    project = models.ForeignKey(Project, to_field='old_id')
    image_ptr_id = models.PositiveIntegerField()
    project_id = models.PositiveIntegerField()
    class Meta:
        db_table = u'images_projectimage'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'
        
class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AccountAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    timezone = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    class Meta:
        db_table = u'account_account'

class AccountOtherserviceinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    key = models.CharField(max_length=50)
    value = models.TextField()
    class Meta:
        db_table = u'account_otherserviceinfo'

class AccountPasswordreset(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    temp_key = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    reset = models.BooleanField()
    class Meta:
        db_table = u'account_passwordreset'

class AnnouncementsAnnouncement(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(AuthUser)
    creation_date = models.DateTimeField()
    site_wide = models.BooleanField()
    members_only = models.BooleanField()
    class Meta:
        db_table = u'announcements_announcement'
        
class TaggitTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=100)
    class Meta:
        db_table = u'taggit_tag'

class TaggitTaggeditem(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.ForeignKey(TaggitTag)
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType)
    class Meta:
        db_table = u'taggit_taggeditem'
        
class PeoplePerson(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    person_type = models.CharField(max_length=100, blank=True)
    joined = models.DateTimeField(null=True, blank=True)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    post_code = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    biography = models.TextField()
    avatar_image = models.CharField(max_length=100)
    class Meta:
        db_table = u'people_person'
        
class PeopleContributor(models.Model):
    person_ptr = models.ForeignKey(PeoplePerson)
    class Meta:
        db_table = u'people_contributor'

class PeopleMember(models.Model):
    person_ptr = models.ForeignKey(PeoplePerson)
    class Meta:
        db_table = u'people_member'

class PeoplePersonSites(models.Model):
    id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'people_person_sites'
        
class PublicationsMagazine(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200)
    class Meta:
        db_table = u'publications_magazine'

class PublicationsMagazineissue(models.Model):
    id = models.IntegerField(primary_key=True)
    magazine = models.ForeignKey(PublicationsMagazine)
    issue_date = models.DateField(null=True, blank=True)
    issue_number = models.PositiveIntegerField(null=True, blank=True)
    issue_month = models.CharField(max_length=100)
    issue_year = models.CharField(max_length=10)
    cover_image = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'publications_magazineissue'
        
class OrganisationsOrganisation(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    created = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_created_by")
    modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_modified_by")
    is_published = models.BooleanField()
    published = models.DateTimeField(null=True, blank=True)
    published_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_ published_by")
    feature = models.BooleanField()
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    post_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=75)
    website = models.CharField(max_length=200)
    website_name = models.CharField(max_length=200)
    logo_image = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'organisations_organisation'

class OrganisationsOrganisationexpertise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    class Meta:
        db_table = u'organisations_organisationexpertise'

class OrganisationsOrganisationOrganisationExpertise(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    organisationexpertise = models.ForeignKey(OrganisationsOrganisationexpertise)
    class Meta:
        db_table = u'organisations_organisation_organisation_expertise'

class OrganisationsOrganisationtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    class Meta:
        db_table = u'organisations_organisationtype'

class OrganisationsOrganisationOrganisationType(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    organisationtype = models.ForeignKey(OrganisationsOrganisationtype)
    class Meta:
        db_table = u'organisations_organisation_organisation_type'

class OrganisationsOrganisationSites(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'organisations_organisation_sites'

class OrganisationsOrganisationTags(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'organisations_organisation_tags'
        
class ProjectsProjectstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=200)
    display = models.TextField()
    class Meta:
        db_table = u'projects_projectstatus'
        
class ProjectsProjectsitetype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    class Meta:
        db_table = u'projects_projectsitetype'
        
class ProjectsProject(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    created = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_created_by")
    modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_modified_by")
    is_published = models.BooleanField()
    published = models.DateTimeField(null=True, blank=True)
    published_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_ published_by")
    project_status = models.ForeignKey(ProjectsProjectstatus, null=True, blank=True)
    client = models.CharField(max_length=200)
    client_website = models.CharField(max_length=200, blank=True)
    client_website_name = models.CharField(max_length=200)
    number_of_stories = models.IntegerField(null=True, blank=True)
    site_type = models.ForeignKey(ProjectsProjectsitetype, null=True, blank=True)
    site_size = models.FloatField(null=True, blank=True)
    building_area = models.FloatField(null=True, blank=True)
    budget_total = models.FloatField(null=True, blank=True)
    design_documentation = models.PositiveIntegerField(null=True, blank=True)
    construction = models.PositiveIntegerField(null=True, blank=True)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    post_code = models.CharField(max_length=10)
    class Meta:
        db_table = u'projects_project'
        
class ProjectsProjecttype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    class Meta:
        db_table = u'projects_projecttype'

class ProjectsProjectcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    class Meta:
        db_table = u'projects_projectcategory'

class ProjectsProjectProjectCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    projectcategory = models.ForeignKey(ProjectsProjectcategory)
    class Meta:
        db_table = u'projects_project_project_categories'

class ProjectsProjectProjectTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    projecttype = models.ForeignKey(ProjectsProjecttype)
    class Meta:
        db_table = u'projects_project_project_types'

class ProjectsProjectSites(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'projects_project_sites'

class ProjectsProjectTags(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'projects_project_tags'

class ProjectsProjectcompany(models.Model):
    id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(ProjectsProject)
    role = models.CharField(max_length=100)
    organisation = models.ForeignKey(OrganisationsOrganisation)
    credit = models.CharField(max_length=200)
    class Meta:
        db_table = u'projects_projectcompany'

class ProjectsProjectdetail(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=200)
    value = models.TextField()
    project = models.ForeignKey(ProjectsProject)
    class Meta:
        db_table = u'projects_projectdetail'

class ProjectsProjectindividual(models.Model):
    id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(ProjectsProject)
    role = models.CharField(max_length=100)
    individual = models.ForeignKey(PeoplePerson)
    credit = models.CharField(max_length=200)
    organisation = models.ForeignKey(OrganisationsOrganisation)
    class Meta:
        db_table = u'projects_projectindividual'

class ProjectsProjectproduct(models.Model):
    id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(ProjectsProject)
    label = models.CharField(max_length=200)
    products = models.TextField()
    class Meta:
        db_table = u'projects_projectproduct'

class ProjectsProjectrole(models.Model):
    id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(ProjectsProject)
    role = models.CharField(max_length=100)
    class Meta:
        db_table = u'projects_projectrole'
        
class ArticlesArticletype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    section = models.CharField(max_length=100)
    class Meta:
        db_table = u'articles_articletype'
        
class ArticlesArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    created = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_created_by")
    modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_modified_by")
    is_published = models.BooleanField()
    published = models.DateTimeField(null=True, blank=True)
    published_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_ published_by")
    feature = models.BooleanField()
    article_type = models.ForeignKey(ArticlesArticletype)
    project = models.ForeignKey(ProjectsProject, null=True, blank=True)
    class Meta:
        db_table = u'articles_article'

class ArticlesArticleContributors(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    person = models.ForeignKey(PeoplePerson)
    class Meta:
        db_table = u'articles_article_contributors'

class ArticlesArticleMagazines(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    magazineissue = models.ForeignKey(PublicationsMagazineissue)
    class Meta:
        db_table = u'articles_article_magazines'

class ArticlesArticleSites(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'articles_article_sites'

class ArticlesArticleTags(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'articles_article_tags'

class ArticlesArticleTagss(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    tag = models.ForeignKey(TaggitTag)
    class Meta:
        db_table = u'articles_article_tagss'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class AvatarAvatar(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    primary = models.BooleanField()
    avatar = models.CharField(max_length=1024)
    date_uploaded = models.DateTimeField()
    class Meta:
        db_table = u'avatar_avatar'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'
        
class DjangoComments(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DjangoContentType)
    object_pk = models.TextField()
    site = models.ForeignKey(DjangoSite)
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=75)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.CharField(max_length=15, blank=True)
    is_public = models.BooleanField()
    is_removed = models.BooleanField()
    class Meta:
        db_table = u'django_comments'

class DjangoCommentFlags(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    comment = models.ForeignKey(DjangoComments)
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    class Meta:
        db_table = u'django_comment_flags'

class DjangoOpenidAssociation(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.TextField()
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()
    class Meta:
        db_table = u'django_openid_association'

class DjangoOpenidNonce(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40)
    class Meta:
        db_table = u'django_openid_nonce'

class DjangoOpenidUseropenidassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    openid = models.CharField(max_length=255)
    created = models.DateTimeField()
    class Meta:
        db_table = u'django_openid_useropenidassociation'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class EmailconfirmationEmailaddress(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    email = models.CharField(max_length=75)
    verified = models.BooleanField()
    primary = models.BooleanField()
    class Meta:
        db_table = u'emailconfirmation_emailaddress'

class EmailconfirmationEmailconfirmation(models.Model):
    id = models.IntegerField(primary_key=True)
    email_address = models.ForeignKey(EmailconfirmationEmailaddress)
    sent = models.DateTimeField()
    confirmation_key = models.CharField(max_length=40)
    class Meta:
        db_table = u'emailconfirmation_emailconfirmation'
        
class EventsEventtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    class Meta:
        db_table = u'events_eventtype'

class EventsEvent(models.Model):
    # feature = models.BooleanField()
    # feature_event = models.BooleanField()
    city = models.CharField(max_length=200)
    content = models.TextField()
    country = models.CharField(max_length=200)
    created = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_created_by")
    email = models.CharField(max_length=75)
    end_date = models.DateField(null=True, blank=True)
    event_type = models.ForeignKey(EventsEventtype, null=True, blank=True)
    fax = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    is_published = models.BooleanField()
    mobile = models.CharField(max_length=200)
    modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_modified_by")
    phone = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    published = models.DateTimeField(null=True, blank=True)
    published_by = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_ published_by")
    slug = models.CharField(max_length=50)
    start_date = models.DateField()
    state = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    summary = models.TextField()
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    website_name = models.CharField(max_length=200)

    class Meta:
        db_table = u'events_event'

class EventsEventSites(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'events_event_sites'

class EventsEventTags(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    tag = models.ForeignKey(TaggitTag)
    class Meta:
        db_table = u'events_event_tags'

class FeaturesFeature(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    active = models.BooleanField()
    ordering = models.PositiveIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'features_feature'

class FeaturesFeaturearea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = u'features_featurearea'

class FeaturesFeatureevent(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    active = models.BooleanField()
    ordering = models.PositiveIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'features_featureevent'

class FeaturesFeatureschedule(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    class Meta:
        db_table = u'features_featureschedule'
        
class ImagesImage(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    caption = models.TextField()
    image = models.CharField(max_length=100)
    feature = models.BooleanField()
    slide_show = models.BooleanField()
    class Meta:
        db_table = u'images_image'

class ImagesArticleimage(models.Model):
    image_ptr = models.ForeignKey(ImagesImage)
    article = models.ForeignKey(ArticlesArticle)
    class Meta:
        db_table = u'images_articleimage'

class ImagesEventimage(models.Model):
    image_ptr = models.ForeignKey(ImagesImage)
    event = models.ForeignKey(EventsEvent)
    class Meta:
        db_table = u'images_eventimage'

class ImagesImageContributor(models.Model):
    id = models.IntegerField(primary_key=True)
    image_id = models.IntegerField()
    person = models.ForeignKey(PeoplePerson)
    class Meta:
        db_table = u'images_image_contributor'

class ImagesProjectimage(models.Model):
    image_ptr = models.ForeignKey(ImagesImage)
    project = models.ForeignKey(ProjectsProject)
    class Meta:
        db_table = u'images_projectimage'

class MailerDontsendentry(models.Model):
    id = models.IntegerField(primary_key=True)
    to_address = models.CharField(max_length=75)
    when_added = models.DateTimeField()
    class Meta:
        db_table = u'mailer_dontsendentry'

class MailerMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    message_data = models.TextField()
    when_added = models.DateTimeField()
    priority = models.CharField(max_length=1)
    class Meta:
        db_table = u'mailer_message'

class MailerMessagelog(models.Model):
    id = models.IntegerField(primary_key=True)
    message_data = models.TextField()
    when_added = models.DateTimeField()
    priority = models.CharField(max_length=1)
    when_attempted = models.DateTimeField()
    result = models.CharField(max_length=1)
    log_message = models.TextField()
    class Meta:
        db_table = u'mailer_messagelog'

class NotificationNoticetype(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40)
    display = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    default = models.IntegerField()
    class Meta:
        db_table = u'notification_noticetype'

class NotificationNotice(models.Model):
    id = models.IntegerField(primary_key=True)
    recipient = models.ForeignKey(AuthUser, related_name="%(app_label)s_%(class)s_recipient")
    sender = models.ForeignKey(AuthUser, null=True, blank=True, related_name="%(app_label)s_%(class)s_sender")
    message = models.TextField()
    notice_type = models.ForeignKey(NotificationNoticetype)
    added = models.DateTimeField()
    unseen = models.BooleanField()
    archived = models.BooleanField()
    on_site = models.BooleanField()
    class Meta:
        db_table = u'notification_notice'

class NotificationNoticequeuebatch(models.Model):
    id = models.IntegerField(primary_key=True)
    pickled_data = models.TextField()
    class Meta:
        db_table = u'notification_noticequeuebatch'

class NotificationNoticesetting(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    notice_type = models.ForeignKey(NotificationNoticetype)
    medium = models.CharField(max_length=1)
    send = models.BooleanField()
    class Meta:
        db_table = u'notification_noticesetting'

class NotificationObserveditem(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    notice_type = models.ForeignKey(NotificationNoticetype)
    added = models.DateTimeField()
    signal = models.TextField()
    class Meta:
        db_table = u'notification_observeditem'

class PopularityViewtracker(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    added = models.DateTimeField()
    viewed = models.DateTimeField()
    views = models.PositiveIntegerField()
    class Meta:
        db_table = u'popularity_viewtracker'

class RegionsRegion(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey(DjangoSite)
    country_code = models.CharField(max_length=10)
    default = models.BooleanField()
    class Meta:
        db_table = u'regions_region'

class SignupCodesSignupcode(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=40)
    max_uses = models.PositiveIntegerField()
    expiry = models.DateTimeField(null=True, blank=True)
    inviter = models.ForeignKey(AuthUser, null=True, blank=True)
    email = models.CharField(max_length=75)
    notes = models.TextField()
    created = models.DateTimeField()
    use_count = models.PositiveIntegerField()
    class Meta:
        db_table = u'signup_codes_signupcode'

class SignupCodesSignupcoderesult(models.Model):
    id = models.IntegerField(primary_key=True)
    signup_code = models.ForeignKey(SignupCodesSignupcode)
    user = models.ForeignKey(AuthUser)
    timestamp = models.DateTimeField()
    class Meta:
        db_table = u'signup_codes_signupcoderesult'

class TopicsTopic(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'topics_topic'

class TopicsTopicalcontent(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DjangoContentType)
    class Meta:
        db_table = u'topics_topicalcontent'

