import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
]
PARLER_DEFAULT_LANGUAGE_CODE = 'en'

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'ar'},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-key-change-in-production')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'cms',
    'pages',
    'jobs',
    'projects',
    'services',
    'core',
]

UNFOLD = {
    "SITE_TITLE": "Bloom Admin",
    "SITE_HEADER": "Bloom Dashboard",
    "SITE_SYMBOL": "🌿",
    "COLORS": {
        "primary": {
            "50": "oklch(98.5% 0.02 145)",
            "100": "oklch(96% 0.04 145)",
            "200": "oklch(92% 0.07 145)",
            "300": "oklch(85% 0.12 145)",
            "400": "oklch(76% 0.16 145)",
            "500": "oklch(66% 0.18 145)",
            "600": "oklch(56% 0.17 145)",
            "700": "oklch(47% 0.15 145)",
            "800": "oklch(38% 0.12 145)",
            "900": "oklch(28% 0.10 145)",
            "950": "oklch(20% 0.08 145)",
        },

        "accent": {
            "50": "oklch(98.5% 0.015 295)",
            "100": "oklch(96% 0.03 295)",
            "200": "oklch(92% 0.06 295)",
            "300": "oklch(85% 0.12 295)",
            "400": "oklch(75% 0.18 295)",
            "500": "oklch(65% 0.22 295)",
            "600": "oklch(55% 0.24 295)",
            "700": "oklch(45% 0.22 295)",
            "800": "oklch(35% 0.18 295)",
            "900": "oklch(25% 0.14 295)",
            "950": "oklch(18% 0.10 295)",
        }
    },
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
}
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
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOCALE_PATHS = [BASE_DIR / 'locale']

CMS_PAGES_APPS = ['pages']
CMS_PLACEHOLDER_CONF = {}
