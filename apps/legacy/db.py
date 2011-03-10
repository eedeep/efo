# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

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

class AdminToolsDashboardPreferences(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    data = models.TextField()
    class Meta:
        db_table = u'admin_tools_dashboard_preferences'

class AdminToolsMenuBookmark(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    class Meta:
        db_table = u'admin_tools_menu_bookmark'

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

class ArticlesArticle(models.Model):
    title = models.CharField(max_length=250, blank=True)
    introduction = models.TextField(blank=True)
    published_by_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    short_title = models.CharField(max_length=250, blank=True)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    modified_by_id = models.IntegerField(null=True, blank=True)
    article_type_id = models.IntegerField(null=True, blank=True)
    created_by_id = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    publisher_id = models.IntegerField(null=True, blank=True)
    slug = models.CharField(unique=True, max_length=50, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'articles_article'

class ArticlesArticleFeatureSets(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    featureset_id = models.IntegerField()
    class Meta:
        db_table = u'articles_article_feature_sets'

class ArticlesArticleMagazines(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    magazineissue_id = models.IntegerField()
    class Meta:
        db_table = u'articles_article_magazines'

class ArticlesArticleSites(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    site_id = models.IntegerField()
    class Meta:
        db_table = u'articles_article_sites'

class ArticlesArticleTags(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'articles_article_tags'

class ArticlesArticleUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = u'articles_article_users'

class ArticlesArticletype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    section = models.CharField(max_length=100)
    class Meta:
        db_table = u'articles_articletype'

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

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

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

class ColophonCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    abbrieviation = models.CharField(max_length=10)
    class Meta:
        db_table = u'colophon_country'

class ColophonPublisher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    class Meta:
        db_table = u'colophon_publisher'

class ColophonSiteprofile(models.Model):
    country_id = models.IntegerField(null=True, blank=True)
    site_id = models.IntegerField(unique=True, null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    abbrieviation = models.CharField(max_length=5, blank=True)
    name = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'colophon_siteprofile'

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

class DjangoCommentFlags(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    comment = models.ForeignKey(DjangoComments)
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    class Meta:
        db_table = u'django_comment_flags'

class DjangoComments(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type_id = models.IntegerField()
    object_pk = models.TextField()
    site_id = models.IntegerField()
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

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoFlatpage(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()
    class Meta:
        db_table = u'django_flatpage'

class DjangoFlatpageSites(models.Model):
    id = models.IntegerField(primary_key=True)
    flatpage_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'django_flatpage_sites'

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

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

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

class EventsEvent(models.Model):
    email = models.CharField(max_length=75, blank=True)
    website_name = models.CharField(max_length=200, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    city = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=250, blank=True)
    introduction = models.TextField(blank=True)
    state = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    suburb = models.CharField(max_length=200, blank=True)
    modified_by_id = models.IntegerField(null=True, blank=True)
    publisher_id = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)
    post_code = models.CharField(max_length=200, blank=True)
    end_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    event_type_id = models.IntegerField(null=True, blank=True)
    published_by_id = models.IntegerField(null=True, blank=True)
    slug = models.CharField(unique=True, max_length=50, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    venue = models.CharField(max_length=200, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    short_title = models.CharField(max_length=250, blank=True)
    summary = models.TextField(blank=True)
    street = models.CharField(max_length=200, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    created_by_id = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'events_event'

class EventsEventSites(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    site_id = models.IntegerField()
    class Meta:
        db_table = u'events_event_sites'

class EventsEventTags(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'events_event_tags'

class EventsEventtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'events_eventtype'

class FeaturesFeature(models.Model):
    feature_set_id = models.IntegerField(null=True, blank=True)
    content_type_id = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'features_feature'

class FeaturesFeatureschedule(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    class Meta:
        db_table = u'features_featureschedule'

class FeaturesFeatureset(models.Model):
    site_feature_area_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    class Meta:
        db_table = u'features_featureset'

class FeaturesSitefeaturearea(models.Model):
    site_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    area = models.CharField(max_length=10)
    class Meta:
        db_table = u'features_sitefeaturearea'

class ImagesArticleimage(models.Model):
    image_ptr_id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    class Meta:
        db_table = u'images_articleimage'

class ImagesEventimage(models.Model):
    image_ptr_id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    class Meta:
        db_table = u'images_eventimage'

class ImagesImage(models.Model):
    image = models.CharField(max_length=200, blank=True)
    slide_show = models.BooleanField(null=True, blank=True)
    feature = models.BooleanField(null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    caption = models.TextField(blank=True)
    user_credit_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    slug = models.CharField(max_length=50, blank=True)
    custom_credit = models.CharField(max_length=200)
    class Meta:
        db_table = u'images_image'

class ImagesProjectimage(models.Model):
    image_ptr_id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    class Meta:
        db_table = u'images_projectimage'

class MailchimpCampaign(models.Model):
    sent_date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    campaign_id = models.CharField(max_length=50, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    content_type_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'mailchimp_campaign'

class MailchimpQueue(models.Model):
    type_opts = models.TextField(blank=True)
    segment_options_all = models.BooleanField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    contents = models.TextField(blank=True)
    subject = models.CharField(max_length=255, blank=True)
    campaign_type = models.CharField(max_length=50, blank=True)
    authenticate = models.BooleanField(null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    from_email = models.CharField(max_length=75, blank=True)
    segment_options = models.BooleanField(null=True, blank=True)
    list_id = models.CharField(max_length=50, blank=True)
    extra_info = models.TextField(blank=True)
    auto_tweet = models.BooleanField(null=True, blank=True)
    from_name = models.CharField(max_length=255, blank=True)
    folder_id = models.CharField(max_length=50, blank=True)
    generate_text = models.BooleanField(null=True, blank=True)
    to_email = models.CharField(max_length=75, blank=True)
    locked = models.BooleanField(null=True, blank=True)
    content_type_id = models.IntegerField(null=True, blank=True)
    tracking_text_clicks = models.BooleanField(null=True, blank=True)
    auto_footer = models.BooleanField(null=True, blank=True)
    tracking_html_clicks = models.BooleanField(null=True, blank=True)
    google_analytics = models.CharField(max_length=100, blank=True)
    segment_options_conditions = models.TextField(blank=True)
    template_id = models.PositiveIntegerField(null=True, blank=True)
    tracking_opens = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'mailchimp_queue'

class MailchimpReciever(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    email = models.CharField(max_length=75)
    class Meta:
        db_table = u'mailchimp_reciever'

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

class NotificationNotice(models.Model):
    id = models.IntegerField(primary_key=True)
    recipient_id = models.IntegerField()
    sender_id = models.IntegerField(null=True, blank=True)
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
    user_id = models.IntegerField()
    notice_type = models.ForeignKey(NotificationNoticetype)
    medium = models.CharField(max_length=1)
    send = models.BooleanField()
    class Meta:
        db_table = u'notification_noticesetting'

class NotificationNoticetype(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40)
    display = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    default = models.IntegerField()
    class Meta:
        db_table = u'notification_noticetype'

class NotificationObserveditem(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    content_type_id = models.IntegerField()
    object_id = models.PositiveIntegerField()
    notice_type = models.ForeignKey(NotificationNoticetype)
    added = models.DateTimeField()
    signal = models.TextField()
    class Meta:
        db_table = u'notification_observeditem'

class OrganisationsOrganisation(models.Model):
    street = models.CharField(max_length=200, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    city = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=250, blank=True)
    introduction = models.TextField(blank=True)
    state = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    suburb = models.CharField(max_length=100, blank=True)
    modified_by_id = models.IntegerField(null=True, blank=True)
    publisher_id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=75, blank=True)
    website = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    logo_image = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    published_by_id = models.IntegerField(null=True, blank=True)
    slug = models.CharField(unique=True, max_length=50, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=200, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    short_title = models.CharField(max_length=250, blank=True)
    summary = models.TextField(blank=True)
    website_name = models.CharField(max_length=200, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    created_by_id = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'organisations_organisation'

class OrganisationsOrganisationOrganisationExpertise(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    organisationexpertise_id = models.IntegerField()
    class Meta:
        db_table = u'organisations_organisation_organisation_expertise'

class OrganisationsOrganisationOrganisationType(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    organisationtype_id = models.IntegerField()
    class Meta:
        db_table = u'organisations_organisation_organisation_type'

class OrganisationsOrganisationSites(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    site_id = models.IntegerField()
    class Meta:
        db_table = u'organisations_organisation_sites'

class OrganisationsOrganisationTags(models.Model):
    id = models.IntegerField(primary_key=True)
    organisation_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'organisations_organisation_tags'

class OrganisationsOrganisationexpertise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'organisations_organisationexpertise'

class OrganisationsOrganisationtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'organisations_organisationtype'

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

class PeoplePersonSites(models.Model):
    id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'people_person_sites'

class PlayFeature(models.Model):
    id = models.IntegerField(primary_key=True)
    feature_set = models.ForeignKey(PlayFeatureset)
    goa = models.ForeignKey(PlayGenericobjectalpha)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    active = models.BooleanField()
    order = models.PositiveIntegerField()
    class Meta:
        db_table = u'play_feature'

class PlayFeatureset(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'play_featureset'

class PlayGenericobjectalpha(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    class Meta:
        db_table = u'play_genericobjectalpha'

class PlayGenericobjectbeta(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    class Meta:
        db_table = u'play_genericobjectbeta'

class PlayGenericobjectbetaFeatureSets(models.Model):
    id = models.IntegerField(primary_key=True)
    genericobjectbeta_id = models.IntegerField()
    featureset = models.ForeignKey(PlayFeatureset)
    class Meta:
        db_table = u'play_genericobjectbeta_feature_sets'

class PopularityViewtracker(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    added = models.DateTimeField()
    viewed = models.DateTimeField()
    views = models.PositiveIntegerField()
    class Meta:
        db_table = u'popularity_viewtracker'

class ProfilesProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    is_contributor = models.BooleanField()
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    biography = models.TextField()
    avatar = models.CharField(max_length=250, blank=True)
    site = models.ForeignKey(DjangoSite, null=True, blank=True)
    class Meta:
        db_table = u'profiles_profile'

class ProjectsProject(models.Model):
    building_area = models.FloatField(null=True, blank=True)
    client_website = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    city = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=250, blank=True)
    introduction = models.TextField(blank=True)
    project_website = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    state = models.CharField(max_length=200, blank=True)
    modified_by_id = models.IntegerField(null=True, blank=True)
    publisher_id = models.IntegerField(null=True, blank=True)
    site_type_id = models.IntegerField(null=True, blank=True)
    design_documentation = models.PositiveIntegerField(null=True, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    project_status_id = models.IntegerField(null=True, blank=True)
    client_website_name = models.CharField(max_length=200, blank=True)
    suburb = models.CharField(max_length=200, blank=True)
    construction = models.PositiveIntegerField(null=True, blank=True)
    number_of_stories = models.IntegerField(null=True, blank=True)
    published_by_id = models.IntegerField(null=True, blank=True)
    slug = models.CharField(unique=True, max_length=50, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=200, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    short_title = models.CharField(max_length=250, blank=True)
    summary = models.TextField(blank=True)
    budget_total = models.FloatField(null=True, blank=True)
    client = models.CharField(max_length=200, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    created_by_id = models.IntegerField(null=True, blank=True)
    site_size = models.FloatField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'projects_project'

class ProjectsProjectProjectCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    projectcategory_id = models.IntegerField()
    class Meta:
        db_table = u'projects_project_project_categories'

class ProjectsProjectProjectTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    projecttype_id = models.IntegerField()
    class Meta:
        db_table = u'projects_project_project_types'

class ProjectsProjectSites(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    site_id = models.IntegerField()
    class Meta:
        db_table = u'projects_project_sites'

class ProjectsProjectTags(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'projects_project_tags'

class ProjectsProjectcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'projects_projectcategory'

class ProjectsProjectcompany(models.Model):
    organisation_id = models.IntegerField(null=True, blank=True)
    credit = models.CharField(max_length=100, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    custom_credit = models.CharField(max_length=255, blank=True)
    role_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'projects_projectcompany'

class ProjectsProjectdetail(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=200)
    value = models.TextField()
    project_id = models.IntegerField()
    class Meta:
        db_table = u'projects_projectdetail'

class ProjectsProjectindividual(models.Model):
    organisation_id = models.IntegerField(null=True, blank=True)
    role_id = models.IntegerField(null=True, blank=True)
    credit = models.CharField(max_length=100, blank=True)
    individual_id = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    custom_credit = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'projects_projectindividual'

class ProjectsProjectproduct(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    label = models.CharField(max_length=200)
    products = models.TextField()
    class Meta:
        db_table = u'projects_projectproduct'

class ProjectsProjectroletype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'projects_projectroletype'

class ProjectsProjectsitetype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'projects_projectsitetype'

class ProjectsProjectstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=200)
    display = models.TextField()
    class Meta:
        db_table = u'projects_projectstatus'

class ProjectsProjecttype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'projects_projecttype'

class PublicationsMagazine(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200)
    class Meta:
        db_table = u'publications_magazine'

class PublicationsMagazineissue(models.Model):
    magazine_id = models.IntegerField(null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    issue_year = models.CharField(max_length=10, blank=True)
    issue_month = models.CharField(max_length=100, blank=True)
    issue_number = models.PositiveIntegerField(null=True, blank=True)
    issue_name = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=100, blank=True)
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    class Meta:
        db_table = u'publications_magazineissue'

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

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        db_table = u'south_migrationhistory'

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

class ThumbnailKvstore(models.Model):
    key = models.CharField(max_length=200, primary_key=True)
    value = models.TextField()
    class Meta:
        db_table = u'thumbnail_kvstore'

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

