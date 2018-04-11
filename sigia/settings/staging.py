from .base import *
import django_heroku


DEBUG = os.environ['DEBUG']
django_heroku.settings(locals())
