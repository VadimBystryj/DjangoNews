"""
Django settings for News project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        'TIMEOUT': 30,
    }
}
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

SECRET_KEY = 'django-insecure-3hd^vqk!8ip9g10a-=o%imc3a)_54&mfac9au-e7%i&0e3q60v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'News_Portal.apps.NewsConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'accounts',
    'fpages',
    'News',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    "django_apscheduler",
]
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = "/posts"
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'News.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
WSGI_APPLICATION = 'News.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SITE_URL = 'http://127.0.0.1:8000'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "BystrouVadzim@yandex.ru"
EMAIL_HOST_PASSWORD = "noaxnxujckgnozvn"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "BystrouVadzim@yandex.ru"
SERVER_EMAIL = "BystrouVadzim@yandex.ru"

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25
MANAGERS = (
    ('Vadim', 'Vadzimbystryj@yandex.ru'),
    ('Vadzim', 'BystrouVadzim@yandex.ru'),
)
ADMINS = (
    ('vadim', 'vadimbystryj@gmail.com'),

)
CELERY_BROKER_URL = 'redis://default:srS6qbbrYbWmM3Ybwv27tIeW5eDtRUc3@redis-15622.c267.us-east-1-4.ec2.cloud.redislabs.com:15622'
CELERY_RESULT_BACKEND = 'redis://default:srS6qbbrYbWmM3Ybwv27tIeW5eDtRUc3@redis-15622.c267.us-east-1-4.ec2.cloud.redislabs.com:15622'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'general_handler', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error_handler', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['error_handler', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['error_handler', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['error_handler', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security_handler'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_debug',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_warning_mail',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_error',
        },
        'general_handler': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'general.log'
        },
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'errors.log',
        },
        'security_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'security.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'form_warning_mail',
        },
    },
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
    },
    'formatters': {
        'form_debug': {
            'format': '{asctime} - [{levelname}] - {message}',
            'style': '{',
        },
        'form_warning_mail': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname}',
            'style': '{',
        },
        'form_error': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} - {exc_info}',
            'style': '{',
        },
        'general_security_info': {
            'format': '{asctime} - [{levelname}] - {message} - {module}',
            'style': '{',
        },
    },
}
