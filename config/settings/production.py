from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    },
}


CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000"
]

DEBUG = False

STATIC_ROOT = os.environ.get('STATIC_ROOT')

STATIC_URL = '/static/'

INSTALLED_APPS += [
]

MIDDLEWARE += [

]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.environ.get('MEDIA_ROOT')

MEDIA_URL = '/media/'


