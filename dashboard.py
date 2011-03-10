from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, NoReverseMatch
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard

# to activate your index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_INDEX_DASHBOARD = 'anow.dashboard.CustomIndexDashboard'

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for anow.
    """
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        
        # append a link list module for "quick links"
        #self.children.append(modules.LinkList(
        #    title=_('Quick links'),
        #    layout='inline',
        #    draggable=False,
        #    deletable=False,
        #    collapsible=False,
        #    css_classes=['column_1'],
        #    children=[
        #        {
        #            'title': _('Return to site'),
        #            'url': '/',
        #        },
        #        {
        #            'title': _('Change password'),
        #            'url': reverse('admin:password_change'),
        #        },
        #        {
        #            'title': _('Log out'),
        #            'url': reverse('admin:logout')
        #        },
        #    ]
        #))
        
        try:
            # add link to filebrowser
            self.children.append(modules.LinkList(
                title=_('Media Management'),
                css_classes=['column_1'],
                children=[
                    {
                        'title': _('Django FileBrowser'),
                        'url': reverse("fb_browse"),
                        'external': False,
                    },
                ]
            ))
        except NoReverseMatch:
            # seems like reverse("fb_browse") didn't worked
            # => filebrowser not installed
            pass
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            title=_('Applications'),
            css_classes=['column_1'],
            exclude_list=('django.contrib', 'colophon',),
        ))
        
        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            title=_('Administration'),
            css_classes=['column_3'],
            include_list=('django.contrib', 'colophon',),
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            css_classes=['column_2'],
            title=_('Recent Actions'),
            limit=5
        ))
        
        # append a feed module
        self.children.append(modules.Feed(
            title=_('Latest Django News'),
            css_classes=['column_2'],
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            title=_('Support'),
            css_classes=['column_3'],
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ]
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass


# to activate your app index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'anow.dashboard.CustomAppIndexDashboard'

class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for anow.
    """
    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # we disable title because its redundant with the model list module
        self.title = ''

        # append a model list module
        self.children.append(modules.ModelList(
            title=_(self.app_title),
            css_classes=['column_1'],
            models=self.models,
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            css_classes=['column_2'],
            include_list=self.get_app_content_types(),
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass
