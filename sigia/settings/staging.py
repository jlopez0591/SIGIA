from .base import *
import django_heroku


DEBUG = os.environ['DEBUG']
STATICFILES_DIRS = ['static']
django_heroku.settings(locals())
