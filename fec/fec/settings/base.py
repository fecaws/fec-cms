"""
Django settings for fec project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

from django.utils.crypto import get_random_string

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
REPO_DIR = os.path.dirname(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taggit',
    'compressor',
    'modelcluster',
    'storages',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailsearch',
    'wagtail.wagtailimages',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailembeds',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.wagtailsearchpromotions',
    'wagtail.contrib.table_block',
    'wagtail.contrib.wagtailstyleguide',

    'fec',
    'search',
    'home',
    'data_loader',
    'uaa_client',
    'extend_admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'uaa_client.middleware.UaaRefreshMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    # logs
    'audit_log.middleware.UserLoggingMiddleware',

)

ROOT_URLCONF = 'fec.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'fec.context.show_settings',
                'fec.context.features',
            ],
        },
    },
]

WSGI_APPLICATION = 'fec.wsgi.application'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_string(50))


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # Be sure to set the DATABASE_URL environment variable on your local
    # development machine so that the local database can be connected to.
    'default': dj_database_url.config()
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'dist', 'fec', 'static'),
    os.path.join(REPO_DIR, 'node_modules', 'fec-style'),
    os.path.join(REPO_DIR, 'node_modules'),
    os.path.join(PROJECT_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'fec.utils.PatchedSCSSCompiler'),
)

# Proxy settings

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Wagtail settings

WAGTAIL_SITE_NAME = "fec"


# Custom settings

from fec import constants
from .env import env

USAJOBS_API_KEY = env.get_credential('USAJOBS_API_KEY')
FEC_APP_URL = os.getenv('FEC_APP_URL')
FEC_API_URL = os.getenv('FEC_API_URL', 'http://localhost:5000')
FEC_API_VERSION = os.getenv('FEC_API_VERSION', 'v1')
FEC_API_KEY_PUBLIC = env.get_credential('FEC_WEB_API_KEY_PUBLIC', '')
FEC_CMS_ROBOTS = os.getenv('FEC_CMS_ROBOTS')
ENVIRONMENTS = {
    'local': 'LOCAL',
    'dev': 'DEVELOPMENT',
    'stage': 'STAGING',
    'prod': 'PRODUCTION',
}
FEC_CMS_ENVIRONMENT = ENVIRONMENTS.get(os.getenv('FEC_CMS_ENVIRONMENT'), 'LOCAL')
CONTACT_EMAIL = 'betafeedback@fec.gov';
CONSTANTS = constants

# Config for the ServiceNow API for contacting RAD
FEC_SERVICE_NOW_API = env.get_credential('FEC_SERVICE_NOW_API')
FEC_SERVICE_NOW_USERNAME = env.get_credential('FEC_SERVICE_NOW_USERNAME')
FEC_SERVICE_NOW_PASSWORD = env.get_credential('FEC_SERVICE_NOW_PASSWORD')

FEC_TRANSITION_URL = env.get_credential('FEC_TRANSITION_URL', 'http://www.fec.gov')
FEC_CLASSIC_URL = env.get_credential('FEC_CLASSIC_URL', 'http://www.fec.gov')

FEATURES = {
    'record': bool(env.get_credential('FEC_FEATURE_RECORD', '')),
    'about': bool(env.get_credential('FEC_FEATURE_ABOUT', '')),
    'agendas': bool(env.get_credential('FEC_FEATURE_AGENDAS', '')),
    'tips': bool(env.get_credential('FEC_FEATURE_TIPS', '')),
    'radform': bool(env.get_credential('FEC_FEATURE_RADFORM', '')),
    'ethnio': bool(env.get_credential('FEC_FEATURE_ETHNIO', '')),
    'site_orientation_banner': bool(env.get_credential('FEC_SITE_ORIENTATION_BANNER'))
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


if FEC_CMS_ENVIRONMENT != 'LOCAL':
    AWS_QUERYSTRING_AUTH = False
    AWS_ACCESS_KEY_ID = env.get_credential('CMS_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env.get_credential('CMS_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env.get_credential('CMS_AWS_STORAGE_BUCKET_NAME')
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_LOCATION = 'cms-content'
    AWS_S3_REGION_NAME = env.get_credential('CMS_AWS_DEFAULT_REGION')

UAA_CLIENT_ID = env.get_credential('CMS_LOGIN_CLIENT_ID', 'my-client-id')
UAA_CLIENT_SECRET = env.get_credential('CMS_LOGIN_CLIENT_SECRET', 'my-client-secret')
#fake uaa server deploys locally on port 8080.  Will be needed to login for local use
#TODO: These will have to have a explicit reference until we can figure out how
#to silence django warnings about the url being http (it expects https).
#UAA_AUTH_URL = env.get_credential('CMS_LOGIN_AUTH_URL', 'http://localhost:8080/oauth/authorize')
#UAA_TOKEN_URL = env.get_credential('CMS_LOGIN_TOKEN_URL','http://localhost:8080/oauth/token')
UAA_AUTH_URL = 'https://login.fr.cloud.gov/oauth/authorize'
UAA_TOKEN_URL = 'https://login.fr.cloud.gov/oauth/token'
WAGTAIL_FRONTEND_LOGIN_URL = 'uaa_client:login'

AUTHENTICATION_BACKENDS = \
    ['django.contrib.auth.backends.ModelBackend',
     'uaa_client.authentication.UaaBackend']

DEFAULT_AUTHENTICATION_CLASSES = ['rest_framework_jwt.authentication.JSONWebTokenAuthentication',]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propogate': False,
        },
    },
}
