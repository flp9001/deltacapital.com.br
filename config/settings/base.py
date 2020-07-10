"""
Django settings for Delta Capital project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import sys
from pathlib import Path

import environ

ROOT_DIR = Path(__file__).parents[2]  # user-records/)
BASE_DIR = str(ROOT_DIR)
APPS_DIR = ROOT_DIR / "apps"  # user-records/)

env = environ.Env(DEBUG=(bool, False))
env.read_env(str(ROOT_DIR / ".env"))

# insert apps folder to sys path: apps don't need to be in project root
sys.path.insert(0, str(ROOT_DIR / "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "iqk^jqy+ewr#%hwt5cq2v0e%u%-+0i9j(6p@4x#*9*+t%y4hl8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)
DEBUG_TEMPLATE = DEBUG

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
]

THIRD_PARTY_APPS = [
    "webpack_loader",
    "compressor",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "constance",  # https://github.com/jazzband/django-constance
    "constance.backends.database",
    "crispy_forms",
    'widget_tweaks',
]


LOCAL_APPS = ["apps.users.apps.UsersConfig", "apps.delta.apps.DeltaConfig"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        # "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "fobi.context_processors.theme",  # Important!
                # "fobi.context_processors.dynamic_values",  # Optional
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
                "admin_tools.template_loaders.Loader",
            ],
            "debug": DEBUG_TEMPLATE,
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


AUTH_USER_MODEL = "users.User"


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
# TIME_ZONE = "UTC"
TIME_ZONE = "America/Fortaleza"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "pt-BR"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(ROOT_DIR / "static")]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = "/media/"
MEDIA_ROOT = str(ROOT_DIR / "media")


WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "webpack_bundles/",  # must end with slash
        "STATS_FILE": str(ROOT_DIR / "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
        "LOADER_CLASS": "webpack_loader.loader.WebpackLoader",
    }
}

COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT


# django-constance
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
# CONSTANCE_DATABASE_CACHE_BACKEND = "default"

CONSTANCE_CONFIG = {
    "WHATSAPP_NUMERO": ("558540422050", "Número de contato Whatsapp"),
    "WHATSAPP_MENSAGEM": (
        "Olá, vi o site DeltaCapital.com.br e gostaria de mais informações.",
        "Texto da mensagem do Whatsapp",
    ),
    "INSTAGRAM_USUARIO": ("delta.capital", "Nome de usuário do Instagram"),
    "FACEBOOK_USUARIO": ("deltacapital.com.br", "Nome de usuário do Facebook"),
}
