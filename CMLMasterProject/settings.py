"""
Django settings for CMLMasterProject project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from YamJam import yamjam
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)
#GET ALL THE PATHS NEEDED
#relative paths for telling the project where templates are house or other special directories
#-getting the location of the settings.py file minus the file itself offcourse
SETTINGS_DIR = os.path.dirname(__file__)
#Go one level up to retrieve the projects directory
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
#for server!!
#PROJECT_PATH = os.path.join(SETTINGS_DIR +"platform/", os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
#create the actual template link to tell the project were the template is
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
#get the static directory for images etc
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATIC_ROOT = os.path.join(STATIC_PATH, 'collectStaticAssets' )
STATIC_URL = '/static/'
#onServer for collectstatic
#STATIC_ROOT = os.path.join(STATIC_PATH, 'collectStaticAssets' )
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    STATIC_PATH,
    os.path.join(BASE_DIR, 'assets'),

)


#Webpack for REACT (GUI library and more support for JS libraries dependency tracking) purposes
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

#celery
CELERY_BROKER_URL = 'amqp://localhost'


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'my_secret'
AUTHENTICATION_KEY_RESEARCH = 'my_authentication_key'
AUTHENTICATION_KEY_STUDENT = 'my_authentication_key'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#on server
#DEBUG = yam_config['debug']


ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PUMA',
    'leaflet',
    'djgeojson',
'bootstrapform',
'CMLMasterProject',
    #wigtail CMS apps
'wagtail.contrib.forms',
'wagtail.contrib.redirects',
'wagtail.embeds',
'wagtail.sites',
'wagtail.users',
#'wagtail.snippets',
'wagtail.documents',
'wagtail.images',
'wagtail.search',
'wagtail.admin',
'wagtail.core',
    'panorama',


'modelcluster',
'taggit',
    'CMS',
"wagtail.contrib.table_block",
    'MicroVis',
'widget_tweaks',
    'rest_framework',
# 'snippets.apps.SnippetsConfig',
    'webpack_loader'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #wigtail CMS
'wagtail.core.middleware.SiteMiddleware',
'wagtail.contrib.redirects.middleware.RedirectMiddleware',

]

ROOT_URLCONF = 'CMLMasterProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CMLMasterProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#PUMA CONFIGURATIONS
LEAFLET_CONFIG = {

 #  'SPATIAL_EXTENT': (4.9597, 52.4551, 4.9, 52.3372),


#'MINIMAP': True,
    'ATTRIBUTION_PREFIX': 'Powered by django-leaflet & IE-SoftLab',

   #'RESET_VIEW': False
}

#media stuff
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
#above defines where media files uploaded should be stored

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

#login -> redirect to home
LOGIN_REDIRECT_URL = '/'
#for server !!
#LOGIN_REDIRECT_URL = '/platform/' -> THIS MIGHT NOT BE NEEDED ANYMORE SO USE '/' DIRECTLY
#wagtail site name of dashboard admin
WAGTAIL_SITE_NAME = 'CML\'s'
