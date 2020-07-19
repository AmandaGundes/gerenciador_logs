from .settings import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.append('whitenoise.middleware.WhiteMoiseMiddleWare')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'