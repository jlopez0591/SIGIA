from .base import *
import django_heroku


DEBUG = False
STATICFILES_DIRS = ['static']
django_heroku.settings(locals())
