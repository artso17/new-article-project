"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from django.urls import reverse
from pathlib import Path
from decouple import config, Csv
import dj_database_url
from dj_database_url import parse as db_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
print(DEBUG)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',



    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'home.apps.HomeConfig',





    'ckeditor',
    'ckeditor_uploader',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'standard',
        'height': 300,
        'width': '100%',
    },
}
CKEDITOR_UPLOAD_PATH = 'uploads'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',


    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'website.wsgi.application'

# allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = config('SITE_ID', default=1, cast=int)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# DATABASE_URL = mysql: // myuser: mypassword@myhost/mydatabase
DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + str(BASE_DIR/'db.sqlite3'),
        cast=db_url
    )
}
if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('db_name'),
            'USER': config('db_user'),
            'PASSWORD': config('db_password'),
            'HOST': config('db_host'),
            # 'PORT':'3306',
        }
    }
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'static_root'

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# whitenoise
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# message


# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD',)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)

# http settings
SESSION_COOKIE_SECURE = config(
    'SESSION_COOKIE_SECURE', cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE',  cast=bool)
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool)


# hsts settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = config(
    'SECURE_HSTS_INCLUDE_SUBDOMAINS',  cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD',  cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int)
print(ALLOWED_HOSTS)

# secure policy
SECURE_REFERRER_POLICY = config('SECURE_REFERRER_POLICY')


# account settings
LOGIN_REDIRECT_URL = '/admin-list/'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
