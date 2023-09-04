from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "True") != "False"

ALLOWED_HOSTS = ["*"]


# Application definition

DEFAULT_APPS = [
    # apps created by django.

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    # apps created in this project.

    "myapp.apps.MyappConfig",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
    #"allauth.socialaccount.providers.twitter",
]

INSTALLED_APPS = [*DEFAULT_APPS, *CUSTOM_APPS, *THIRD_PARTY_APPS]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
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

WSGI_APPLICATION = 'oauth.wsgi.application'

AUTH_USER_MODEL = "myapp.User"


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Allauth Configurations

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",

    # allauth
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "facebook": {
        "APP": {
            "client_id": os.environ.get("FACEBOOK_SECRET"),
            "key": os.environ.get("FACEBOOK_KEY"),
        },
        "METHOD": "oauth2",
        "SCOPE": ["email", "username", "public_profile"],
        #"SDK_URL": "//connect.facebook.net/{locale}/sdk.js",
        #"AUTH_PARAMS": {"auth_type": "reauthenticate"},
        "INIT_PARAMS": {"cookie": True},
        "FIELDS": [
            "username",
            "email",
            "id",
            "first_name",
            "last_name",
        ],
        #"EXCHANGE_TOKEN": True,
        "VERIFIED_EMAIL": False,
        "VERSION": "v13.0",
        "GRAPH_API_URL": "https://graph.facebook.com/v13.0"
    },
    "github": {
        "APP": {
            "client_id": os.environ.get("GITHUB_KEY"),
            "secret": os.environ.get("GITHUB_SECRET"),
        },
        "SCOPE": [
            "user"
        ]
    },
    "google": {
        "APP": {
            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
            "secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
        },
        "SCOPE": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {
            "access_type": "offline"
        },
        "OAUTH_PKCE_ENABLED": True
    }
}
