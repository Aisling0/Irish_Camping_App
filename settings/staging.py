from base import *
import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


# Stripe
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_IwUXtl7a8TYJdu9S4anEHWyi')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_mLeYQydSoe76bOTxhd4dCIYM')


SITE_URL = 'https://irish-camping.herokuapp.com'
ALLOWED_HOSTS.append('irish-camping.herokuapp.com')


# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
