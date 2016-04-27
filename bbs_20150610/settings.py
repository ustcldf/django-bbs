"""
Django settings for wenda project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p8$cw)we--%9qxsmvqok6n3k72z@iwg-o3g1n@qa9$ga^e6fy='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    'tastypie',
    'pagination',
    'apps.notifications',
    'apps.attachments',
    'apps.home',
    'apps.account',
    'apps.question',
    'apps.district',
    'apps.forum',
    'apps.article',
    'apps.tag',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'pagination.middleware.PaginationMiddleware',
)


AUTHENTICATION_BACKENDS = (
    'apps.account.backend.CasBackend',
    'django.contrib.auth.backends.ModelBackend',)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                "context_processors.config",
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# HOST_IP = "192.168.146.137"
HOST_IP = "127.0.0.1"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'BBS',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': 'z',  # Not used with sqlite3.
        'HOST': HOST_IP,  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TASTYPIE_DEFAULT_FORMATS = ['json']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": '/static/bower_components/jquery/dist/jquery.js'
}

USERENA_REMEMBER_ME_DAYS = 7 * 86400,

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = "/media/"
ATTACHMENT_UPLOAD_TO = 'attachments'
AVATARS_UPLOAD_TO = "avatars"
DISTRICT_ICON_UPLOAD_TO = "icons"



NOTIFICATION_USER = 1
LOGIN_URL = '/account/login/'
# =====


class PaginationSettings(object):
    def __getattr__(self, attr):
        return {
            "reply": 12
        }.get(attr, 12)


DEFAULT_PAGINATION = PaginationSettings()

HOME_PAGE = "http://10.3.30.199:8000/"
SIGNIN_BACK = HOME_PAGE + "account/casuserget/"
auth_uri = "http://10.3.30.13:30080/"
# =========cas=========
CAS_SETTINGS = {
        "client_id": "BtymYCSy7Jk0GIQhxQ?YHrtJKttB@aRpLrbUlXxV",
        "client_secret": "lRgyRPQOlIJ0JnN5oQ6ks3nd0_ttq__h7rrJQ5kC21@Zz=yqRHsuH5o.FPd;bTD?-SPlpTKoF2FYqFC-nPUCo33Gz4454bQ??9tBD?uZrWnZw.ZWdy4F2sW@qq9LMXW5",
        "auth_uri": auth_uri,
        "redirect_uri": SIGNIN_BACK,
        "authorization_uri": "%soauth2/authorize/" % auth_uri,
        "token_uri": "%soauth2/token/" % auth_uri,
        "openid_uri": "%soauth2/me/" % auth_uri,
        "user_api_uri": "%soauth2/api/v1/user/" % auth_uri,
}
