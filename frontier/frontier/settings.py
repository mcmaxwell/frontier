"""
Django settings for skelet project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
import cloudinary


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4$6(ctt7gg0(l((l0qfp==40js#um4)5=vj&4#o+dv)2e4g4wl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #libs
    'redactor',
    'sorl.thumbnail',
    'adminsortable2',
    'modeltranslation',
    'django_summernote',
    'sortedm2m',

    # feincms
    'feincms',
    'mptt',
    'feincms.module.page',

    # local apps
    'common',
    'content',
    'news',
    'info',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
  #  'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'frontier.helpers.AdminLocaleMiddleware'
)

ROOT_URLCONF = 'frontier.urls'

ADMIN_LANGUAGE_CODE = 'en-EN'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontier/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'info.context_processors.info',
                'info.context_processors.links',
            ],
        },
    },
]

WSGI_APPLICATION = 'frontier.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'frontier',
        'USER': 'django',
        'PASSWORD': '1qw23er4',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'nb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    #('ru', _('Russian')),
    ('no', _('Norwegian')),
    ('en', _('English')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale/"),
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
#STATIC_URL = 'https://s3.eu-west-2.amazonaws.com/frontier/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../dev/static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media',)
MEDIA_URL = '/media/'

# MODULES OPTIONS

REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD = 'uploads/'

THUMBNAIL_COLORSPACE = None

THUMBNAIL_PRESERVE_FORMAT = True

SUMMERNOTE_CONFIG = {

    'attachment_filesize_limit': 10000000 * 1024,

    'width': 800,
    'height': 570,

    'toolbar': [
        ['style', ['style']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['font', ['bold', 'italic', 'underline',
                  'clear']],
        ['height', ['height']],
        ['insert', ['link', 'picture', 'hr']],
        ['view', ['fullscreen', 'codeview']],
        ['help', ['help']],
        ['insert', ['link']],
        ],

 }



try:
    from local_settings import *
except ImportError:
    pass