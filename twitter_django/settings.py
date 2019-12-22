import os

import dj_database_url
from decouple import Csv, config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
SECRET_KEY = config('SECRET_KEY')


DEBUG = config('DEBUG', default=True, cast=bool)


ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'data.apps.DataConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'twitter_django.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'twitter_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL) }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': '',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Redirect users after login/logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# Email configuration for file based development backend
DEFAULT_FROM_EMAIL = 'admin@tweetdash.com'
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")


# Exntending the default User model
AUTH_USER_MODEL = 'accounts.CustomUser'


# Celery configuration
BROKER_URL = config('REDIS_URL')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = config('CELERY_ACCEPT_CONTENT')
CELERY_TASK_SERIALIZER = config('CELERY_TASK_SERIALIZER')
CELERY_RESULT_SERIALIZER = config('CELERY_RESULT_SERIALIZER')


#Twitter API credentials
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
