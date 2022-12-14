"""
Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import requests

from django_admin_auth_sso.support.django_helpers import getenv_or_raise_exception

SRC_DIR = Path(__file__).resolve().parent
BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from dotenv import load_dotenv

    load_dotenv(BASE_DIR.joinpath(".env.development"), verbose=True)
except ImportError:
    pass


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z8ath-&@*v6i1&=28(zh_!_(m2#u(0@*39_c)1*aat4dc$xv^k"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "mozilla_django_oidc",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_admin_auth_sso.apps.core",
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

# https://docs.djangoproject.com/en/4.0/ref/settings/#authentication-backends

AUTHENTICATION_BACKENDS = [
    # Leave ModelBackend here if you want to allow "username/password" authentication
    "django.contrib.auth.backends.ModelBackend",
    "django_admin_auth_sso.support.oidc_helpers.CustomOIDCAuthenticationBackend",
]

ROOT_URLCONF = "django_admin_auth_sso.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [SRC_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_admin_auth_sso.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuration to enable SSO on Django Admin!
# https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html#quick-start

BASE_URL = "http://localhost:8000" #os.getenv("BASE_URL", "http://app.local:8000")

ONLOGIN_DOMAIN = "YOUR_ONELOGIN_DOMAIN"  # onelogin domain  xxx.onelogin.com/oidc/2
ONELOGIN_LOGOUT_ENDPOINT = f"https://{ONLOGIN_DOMAIN}/logout"

OIDC_RP_CLIENT_ID = "YOUR_CLIENT_ID" 
OIDC_RP_CLIENT_SECRET = "YOUR_CLIENT_SECRET" 

ALLOW_LOGOUT_GET_METHOD = True
LOGIN_REDIRECT_URL = f"{BASE_URL}/admin/"
LOGOUT_REDIRECT_URL = f"{BASE_URL}/admin/logout/"
OIDC_OP_JWKS_ENDPOINT = f"https://{ONLOGIN_DOMAIN}/certs"
OIDC_RP_SIGN_ALGO = "RS256"
#OIDC_OP_LOGOUT_URL_METHOD = "django_admin_auth_sso.support.oidc_helpers.provider_logout"

OIDC_OP_AUTHORIZATION_ENDPOINT = f"https://{ONLOGIN_DOMAIN}/auth"
OIDC_OP_TOKEN_ENDPOINT = f"https://{ONLOGIN_DOMAIN}/token"
OIDC_OP_USER_ENDPOINT = f"https://{ONLOGIN_DOMAIN}/me"
OIDC_RP_SCOPES = "openid profile email"
OIDC_VERIFY_SSL = True