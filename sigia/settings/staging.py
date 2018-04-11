from .base import *
import django_heroku


DEBUG = False
IMPLEMENT_HEROKU = True
STATICFILES_DIRS = ['static']
django_heroku.settings(locals())
