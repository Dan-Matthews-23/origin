
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+uoc2^fkz%=k@(7nv(&e*i9vxjneu%krmcxj457$a@-1=tyftb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['8000-danmatthews23-origin-819o9ejp1tg.ws.codeinstitute-ide.net']
CSRF_TRUSTED_ORIGINS = ['https://8000-danmatthews23-origin-819o9ejp1tg.ws.codeinstitute-ide.net']


# Application definition




INSTALLED_APPS = [
    'django.contrib.admin',    
    'django.contrib.contenttypes',
    'django.contrib.sessions',    
    'django.contrib.staticfiles',     
    'django.contrib.auth',
    'django.contrib.messages',
    'allauth',
    'allauth.account',
    'home',
    'production',
    'user_account',
    'diplomacy',
    'fight',
    'military',
    'crispy_forms',
    'crispy_bootstrap5',
    'faction_data',
    'player_power',
    'turn_events',
    'technology',
    'reports',
    'error_log',
    'game_settings',
]
    




MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
)

ROOT_URLCONF = 'origin.urls'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.active_user_count',
                'home.context_processors.data_crystal_balance',
                
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]

        },
    },
]

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'overview'


WSGI_APPLICATION = 'origin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




BASE_POP_INCREASE_COST = 2000





"""
TRUE BIAS SETTINGS
Calculated as:
- If an attacker's intelligence power is at least 50% higher than the defender, the operation will always be a success
- If an attacker's intelligence power is at least 25% higher than the defender, the operation has a 70% of being successfull
- If an attacker's intelligence power is higher than the defender's, but less than 25% higher, the operation has a 50% of being successfull
"""
TRUE_BIAS_TWENTY_FIVE_PERCENT = 0.7
TRUE_BIAS_LESS_TWENTY_FIVE_PERCENT = 0.5

"""
    Intel Troops Loss base
"""
BASE_INTEL_LOSS_OVERWHELMING = 0
BASE_INTEL_LOSS_CLEAR = 0.25
BASE_INTEL_LOSS_VICTORY = 0.50

BASE_INTEL_LOSS_DEFEAT_OVERWHELMING = 0
BASE_INTEL_LOSS_DEFEAT_CLEAR = 0.25
BASE_INTEL_LOSS_DEFEAT_LOSS = 0.50


"""
    Attack Troops Loss base
"""



ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK = 0
DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK = 0.5
INCOME_GAIN_FOR_OVERWHELMING_SUCCESS_ATTACK = 85

ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK = 0.15
DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK = 0.25
INCOME_GAIN_FOR_CLEAR_SUCCESS_ATTACK = 70

ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK = 0.25
DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK = 0.35
INCOME_GAIN_FOR_NARROW_SUCCESS_ATTACK = 60




ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK = 0.5
DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK = 0

ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK = 0.25
DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK = 0.15

ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK = 0.35
DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK = 0.25








