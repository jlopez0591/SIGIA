from sigia.base_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sigia_db',
        'USER': 'sigia_user',
        'PASSWORD': '22WQYfJa4uloeWeyaa2d',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True
ALLOWED_HOSTS = ['10.0.1.151',]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

