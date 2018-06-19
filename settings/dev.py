from base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


INSTALLED_APPS.append('debug_toolbar')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Stripe Variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_IwUXtl7a8TYJdu9S4anEHWyi')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_mLeYQydSoe76bOTxhd4dCIYM')
