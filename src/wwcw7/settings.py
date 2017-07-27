import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Women Who Code Team', 'admin@wwcw7.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'wwcw7_test',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Kuala_Lumpur'
LANGUAGE_CODE = 'en'

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
)

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = ''
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'htdocs/static'),
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '$5$QJdi4pOT6Q$1Dpq5ifaZM9pB3yn5b.OOvBaL5Hztq6G1cQbl1CoSyC'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'wwwcw7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'htdocs')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'allauth',
    'allauth.account',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.ERROR : 'danger',
}

ACCOUNT_USERNAME_REQUIRED               = False
ACCOUNT_EMAIL_REQUIRED                  = True
ACCOUNT_EMAIL_VERIFICATION              = "none"
ACCOUNT_UNIQUE_EMAIL                    = True
ACCOUNT_AUTHENTICATION_METHOD           = "email"



