from .base import *
DEBUG=True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sigia',
        'USER': 'sigia_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SECRET_KEY = os.environ['SECRET_KEY']
STATICFILES_DIRS = [root('static'), ]
