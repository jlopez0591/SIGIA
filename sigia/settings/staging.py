from .base import *
import django_heroku


DEBUG = True
IMPLEMENT_HEROKU = True
STATICFILES_DIRS = ['static']
django_heroku.settings(locals())
