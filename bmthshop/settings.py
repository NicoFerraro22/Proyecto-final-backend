import os
import pymysql
from pathlib import Path

pymysql.install_as_MySQLdb()

# ===========================
# BASE
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")  
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "https://proyecto-final-backend-production-9af8.up.railway.app"],



# ===========================
# APPS
# ===========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Third party
    "rest_framework",
    "corsheaders",

    # Local apps
    "catalog",
]

# ===========================
# TEMPLATES (NECESARIO PARA ADMIN)
# ===========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


# ===========================
# MIDDLEWARE
# (WhiteNoise debe estar después de SecurityMiddleware)
# ===========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # <--- IMPORTANTE
    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ===========================
# URLS & WSGI
# ===========================

ROOT_URLCONF = "bmthshop.urls"

WSGI_APPLICATION = "bmthshop.wsgi.application"


# ===========================
# BASE DE DATOS (Railway MySQL)
# ===========================

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", ""),
        "PORT": os.environ.get("DB_PORT", ""),
    }
}


# ===========================
# REST FRAMEWORK + JWT
# ===========================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}


# ===========================
# CORS
# ===========================

CORS_ALLOW_ALL_ORIGINS = True


# ===========================
# INTERNATIONAL
# ===========================

LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True


# ===========================
# STATIC & MEDIA (PRODUCCIÓN)
# ===========================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ===========================
# AUTO FIELD
# ===========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
