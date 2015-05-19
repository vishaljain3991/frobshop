"""
Django settings for frobshop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from oscar import get_core_apps
from oscar.defaults import *
from password import secret
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'debug_toolbar',
    'paypal',
    'compressor',


] + get_core_apps(['myapp.order', 'myapp.catalogue', 'myapp.checkout',])
SITE_ID = 1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)


ROOT_URLCONF = 'frobshop.urls'

WSGI_APPLICATION = 'frobshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'craft',
        'USER': 'ecom',
        'PASSWORD': '9957608275',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)

from oscar import OSCAR_MAIN_TEMPLATE_DIR

#location = lambda x: os.path.join(
#   os.path.dirname(os.path.realpath(__file__)), x)
    
    
    
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)

TEMPLATE_DIRS = (
    location('templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}
OSCAR_FROM_EMAIL='vishaljainthebest@gmail.com'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = location("public/media/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/admin/'
#OSCAR_MISSING_IMAGE_URL = MEDIA_URL + 'image_not_found.jpg'

STATIC_URL = '/static/'
STATIC_ROOT = location('public/static/')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    "/home/vishal/oscar_2/frobshop/static",
)
COMPRESS_ENABLED = True
USE_LESS = False
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_OFFLINE_CONTEXT = {
    # this is the only default value from compressor itself
    'STATIC_URL': STATIC_URL,
    'use_less': USE_LESS,
}

THUMBNAIL_DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'oscar.checkout': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'paypal.express': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'paypal.payflow': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

OSCAR_SHOP_NAME = 'CultIndus'

OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('PayFlow transactions'),
                'url_name': 'paypal-payflow-list',
            },
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    })


# Taken from PayPal's documentation - these should always work in the sandbox
PAYPAL_SANDBOX_MODE = True
PAYPAL_CALLBACK_HTTPS = False
PAYPAL_API_VERSION = '119'

# These are the standard PayPal sandbox details from the docs - but I don't
# think you can get access to the merchant dashboard.
PAYPAL_API_USERNAME = 'vishaljainthebest_api1.gmail.com'
PAYPAL_API_PASSWORD = 'MM7XUP4EQT3QUGWU'
PAYPAL_API_SIGNATURE = 'ArYFHXOXjn34pCIr6guS8X9h-L7UAjMptfnHPOeFQa68IkuqI1A4QZi-'

# Standard currency is GBP
PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'GBP'
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True

PAYPAL_PAYFLOW_VENDOR_ID = 'vishaljainthebest'
PAYPAL_PAYFLOW_PASSWORD = 'mdG6GNuU'
# Put your own sandbox settings into an integration.py modulde (that is ignored
# by git).
try:
    from integration import *  # noqa
except ImportError:
    pass
