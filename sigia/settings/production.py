from .base import *

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '',
    }
}


STATIC_DIR = root('static')
ALLOWED_HOSTS = ['10.0.1.151',] # Este debe ser el valor del URL o IP del servidor
