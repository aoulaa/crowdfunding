import os
import sys
from pathlib import Path

from django.conf import settings
from dotenv import load_dotenv

# Path to your .env file
dotenv_path = os.path.join(Path(__file__).resolve().parent.parent.parent, '.env')

load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'local')

DEBUG = os.getenv('DJANGO_DEBUG', True)



# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "files/static")


if os.environ.get('MEDIA_ROOT'):
    MEDIA_ROOT = os.environ.get('MEDIA_ROOT')
else:
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'mediafiles')

# URL used to access the media
MEDIA_URL = '/media/'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS')
if ALLOWED_HOSTS and isinstance(ALLOWED_HOSTS, str):
    ALLOWED_HOSTS = ALLOWED_HOSTS.split(",")
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CORS_ORIGIN_WHITELIST = os.getenv('DJANGO_CORS_ORIGIN_WHITELIST')
if CORS_ORIGIN_WHITELIST and isinstance(CORS_ORIGIN_WHITELIST, str):
    CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST.split(",")
else:
    CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://127.0.0.1"]

CSRF_TRUSTED_ORIGINS = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS')
if CSRF_TRUSTED_ORIGINS and isinstance(CSRF_TRUSTED_ORIGINS, str):
    CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS.split(",")
else:
    CSRF_TRUSTED_ORIGINS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django rest

    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",  # add google auth https://testdriven.io/blog/django-rest-auth/
    "dj_rest_auth",
    "dj_rest_auth.registration",

    # apps
    'core',
    'project',
    'authentication',
    'users',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}

# Password validation

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

# django rest_framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ]

}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

ACCOUNT_AUTHENTICATION_METHOD = "email"  # Use Email / Password authentication
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # or none
ACCOUNT_MAX_EMAIL_ADDRESSES = 2

# <EMAIL_CONFIRM_REDIRECT_BASE_URL>/<key>
EMAIL_CONFIRM_REDIRECT_BASE_URL = os.getenv("EMAIL_CONFIRM_REDIRECT_BASE_URL")

# <PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL>/<uidb64>/<token>/
PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = os.getenv("PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")  # smtp-relay.sendinblue.com
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"  # False
EMAIL_PORT = os.getenv("EMAIL_PORT")  # 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")  # your email address
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # your password
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")  # email ending with @sendinblue.com
