
# -*- coding: utf-8 -*-
# Django settings for basic pinax project.

import os.path
import posixpath
import pinax
import grappelli
import sys

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
GRAPPELLI_ROOT = os.path.abspath(os.path.dirname(grappelli.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_FOLDER = os.path.dirname(__file__).split('/')[-1]
sys.path.insert(0, os.path.join(PROJECT_ROOT))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# tells Pinax to use the default theme
PINAX_THEME = "pinax-designer-theme"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

CONTACT_EMAIL = 'info@architecturenow.com.au'

MANAGERS = ADMINS

# Default DB settings -- override in local_settings.py (currently included in .hgignore)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": os.path.join(PROJECT_ROOT, "dev.db"),                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Australia/Melbourne"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

SITE_NAME = "Architecture Now"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "media"),
    os.path.join(PROJECT_ROOT, "media", PINAX_THEME), # ship 'with' the project for now.
    # revert to the Pinax default whilst design_five is in development
    os.path.join(PINAX_ROOT, "media", "default"),
    
    # include grappelli
    ("admin", os.path.join(GRAPPELLI_ROOT, "media")),
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")
ADMIN_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'admin')

# Make this unique, and don't share it with anybody.
SECRET_KEY = "unzj&n1$^ox6%-xh490357i=l@wmq!lu&toe=*sj8s2qv73mhr"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pinax.apps.account.middleware.LocaleMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "meta.middleware.AppMetaMiddleware",
    # "base.middleware.ObjectListFilterMiddleware"
    
    "colophon.middleware.MultiHostMiddleware",
]

ROOT_URLCONF = PROJECT_FOLDER + ".urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PROJECT_ROOT, "templates", PINAX_THEME), # ship 'with' the project for now.
    # revert to the Pinax default whilst design_five is in development
    os.path.join(PINAX_ROOT, "templates", "default")
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    
    "staticfiles.context_processors.static_url",
    
    "pinax.core.context_processors.pinax_settings",
    
    "pinax.apps.account.context_processors.account",
    
    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    
    'popularity.context_processors.most_popular',
    'popularity.context_processors.most_viewed',
    'popularity.context_processors.recently_viewed',
    'popularity.context_processors.recently_added',
    
    # 'meta.context_processors.verbose_app_label',
    
    'grappelli.context_processors.admin_template_path',
    
    'django.core.context_processors.request',
    'colophon.context_processors.multihost',
]

INSTALLED_APPS = [
    # external
    "notification", # must be first
    
    # admin
    'grappelli',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.databrowse",
    "django.contrib.comments",
    "django.contrib.contenttypes",
    # "django.contrib.flatpages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    
    "pinax.templatetags",
    
    # external cont'd
    "staticfiles",
    "debug_toolbar",
    "django_extensions",
    "mailer",
    "uni_form",
    "django_openid",
    "ajax_validation",
    "timezones",
    "emailconfirmation",
    "announcements",
    "pagination",
    "idios",
    "endless_pagination",
    
    # Pinax
    "pinax_local.apps.account",
    # "pinax.apps.signup_codes",
    "pinax.apps.analytics",
    
    # project
    "about",
    "profiles",
    
    # ANow
    'articles',
    'ads',
    'base',
    'colophon',
    'events',
    'features',
    'images',
    'inbox',
    'landings',
    'organisations',
    'projects',
    'publications',
    'regions',
    'search',   
    'staging', 
    'topics',
    'archive',
    
    # 'play',
    
    # libraries
    
    'antony',
    'meta',
    
    # django
    
    # 'avatar',
    # 'easy_maps',
    'filebrowser',
    'flatpages', # from django dev version 1.3
    'mailchimp',
    'sorl.thumbnail',
    'popularity',
    'south',
    'taggit',
    'tags',
    #'tinymce',
    
    # libraries
    
    'antony',
    'meta',

    # 'uwsgi_admin'
]

# Database

DATABASE_ROUTERS = [
]

# Fixtures
FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

# Messages
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/%s/" % o.username,
}

# Accounts / Profiles
AUTH_PROFILE_MODULE = "profiles.Profile"

NOTIFICATION_LANGUAGE_MODULE = "account.Account"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_AUTHENTICATION = True
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    "profiles.auth_backends.AuthenticationBackend",
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "home"

# Admin Tools
ADMIN_TOOLS_INDEX_DASHBOARD = PROJECT_FOLDER + '.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = PROJECT_FOLDER + '.dashboard.CustomAppIndexDashboard'

# Debugging Toolbar
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# Filebrowser
FILEBROWSER_DEBUG = False
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/'
FILEBROWSER_PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'
FILEBROWSER_DIRECTORY = 'files/'

FILEBROWSER_SAVE_FULL_URL = False
FILEBROWSER_VERSIONS_BASEDIR = "cache"

# Google Analytics
# URCHIN_ID = "ua-..."

# Grappelli
GRAPPELLI_ADMIN_TITLE = 'Architecture Now' 
GRAPPELLI_ADMIN_URL = '/admin'

# Mailchimp
# MAILCHIMP_API_KEY = '512d0fd3f9f86c51405f4bf2984132e3-us1' # Label Architecture Now
# MAILCHIMP_WEBHOOK_KEY = '!Arch1t3ctur3N0w'
# MAILCHIMP_LIST_ID = '789ab49070' # For 'Architecture Now'

# Sorl Thumbnail
THUMBNAIL_BASEDIR = "cache"
THUMBNAIL_DEBUG = False

# Local Settings
try:
    from local_settings import *
except ImportError:
    pass

# @@@ To be moved to entropy

PUBLISHER_COUNTRIES = OWNER_COUNTRIES = (
    ('AU', (u'Australia')),
    ('NZ', (u'New Zealand'))
)