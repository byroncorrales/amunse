# Django settings for simas project

from settings_local import *

DEBUG = True 
TEMPLATE_DEBUG = DEBUG
DEFAULT_CHARSET = 'utf-8'
MANAGERS = ADMINS
DATABASE_ENGINE = 'mysql'
SEARCH_ENGINE = 'mysql'
ACCOUNT_ACTIVATION_DAYS = 7
SITE_ID = 1
USE_I18N = True
ADMIN_MEDIA_PREFIX = '/archivos/admin/'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
 #   'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)


MEDIA_ROOT = os.path.join(SITE_ROOT,'media')
MEDIA_URL = '/archivos/'
TEMPLATE_DIRS = (
SITE_ROOT+"/templates",
)
ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS=("django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "context.elementos_fijos",
    )

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'documentos',
    'south',
    'tagging',
    'tagging_autocomplete',
    'noticias',
    'multimedia',
    'eventos',
    'videos',
    'boletines',
    'revistas',
    'paginas',
    'municipios',
    'proyectos',

)

