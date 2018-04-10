from sigia.main import *
import django_heroku

django_heroku.settings(locals())

DEBUG = False

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

TEST_RUNNER = 'django_heroku.HerokuDiscoverRunner'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'