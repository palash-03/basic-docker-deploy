from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'scrap',
        'USER': 'postgres',
        'PASSWORD': '12345',
        # 'HOST': '127.0.0.1',
        'HOST': 'db',
        'PORT': '5432',
    }
}