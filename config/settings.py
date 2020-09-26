"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b#s*_o(3t3ai_k(c5po@h7a=nj5#vjkd3u7ckhnx@)mi=8fn67'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True" and True or False

ALLOWED_HOSTS = []



# Application definition



DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
  "core.apps.CoreConfig",
  "users.apps.UsersConfig",
  "books.apps.BooksConfig",
  "categories.apps.CategoriesConfig",
  "favs.apps.FavsConfig",
  "movies.apps.MoviesConfig",
  "people.apps.PeopleConfig",
  "reviews.apps.ReviewsConfig"
]

THIRD_PARTY_APPS = [
  "django_seed",
  "storages",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("RDS_HOST"),
            "NAME": os.environ.get("RDS_NAME"),
            "PASSWORD": os.environ.get("RDS_PASSWORD"),
            "PORT": "5432",
            "USER": os.environ.get("RDS_USER"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

if not DEBUG:
    sentry_sdk.init(
        dsn="https://1ab29b256e884d849696c1295fa1f9fb@o438795.ingest.sentry.io/5440873",
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
    DEFAULT_FILE_STORAGE = 'config.custom_storages.StaticStorage'
    STATICFILES_STORAGE = 'config.custom_storages.UploadsStorage'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_ID")
    AWS_SECRET_ACCESS_KEY =os.environ.get("AWS_ACCESS_SECRET")
    AWS_STORAGE_BUCKET_NAME = "django-challenge-storage"
    AWS_AUTO_CREATE_BUCKET = True
    AWS_BUCKET_ACL = "public-read"
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    MEDIA_ROOT = f"https://{AWS_S3_CUSTOM_DOMAIN}/uploads/"
    MEDIA_URL = "/media/"
    

else:
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
    MEDIA_URL = "/media/"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

ALLOWED_HOSTS = ['*']
X_FRAME_OPTIONS = '*'



AUTH_USER_MODEL = "users.User"