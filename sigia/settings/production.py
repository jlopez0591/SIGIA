from sigia.settings.main import *

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

DEBUG = False
ALLOWED_HOSTS = ['10.0.1.151',]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

