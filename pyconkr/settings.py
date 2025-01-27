import datetime
import os

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b6&$e@3d_5xorj*ipg-%=bbsy#a3bryr)^45jnhhik%yjm*sqk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
SITE_ID = 1

INSTALLED_APPS = (
    # django apps
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.humanize',
) + (
    # thirt-party apps
    'django_summernote',
    'rosetta',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    'sorl.thumbnail',
    'constance',
    'constance.backends.database',
    'django_csv_exports',
    'mail_templated',
    'import_export',
) + (
    # local apps
    'pyconkr',
    'announcement',
    'user',
    'sponsor',
    'program',
    'registration',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyconkr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "pyconkr/templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pyconkr.context_processors.default',
                'pyconkr.context_processors.sponsors',
                'pyconkr.context_processors.profile',
                'constance.context_processors.config',
            ],
        },
    },
]


WSGI_APPLICATION = 'pyconkr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.getenv('POSTGRES_NAME'):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_NAME'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    }
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGES = (
    ('ko', _('Korean')),
    ('en', _('English')),
)
LANGUAGE_CODE = 'ko'
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': ('ko', 'en'),
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'pyconkr', 'locale'),
)

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FORCE_SCRIPT_NAME = ''
APPEND_SLASH = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "pyconkr/static"),
# )
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    # From 2019 we have decided to support github/facebook login
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_URL = '/2020/login/'
LOGIN_REDIRECT_URL = '/2020/profile/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = False
# SOCIALACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

if os.getenv('EMAIL_HOST_USER'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = 'PyCon Korea <pyconkr@pycon.kr>'


DOMAIN = ''

CRISPY_TEMPLATE_PACK = 'bootstrap3'


def static_url(url):
    return os.path.join(STATIC_URL, url)


SUMMERNOTE_CONFIG = {
    'width': '100%',
    'toolbar': [
        ['insert', ['emoji']],
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript',
                  'strikethrough', 'clear']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video', 'hr']],
        ['view', ['fullscreen', 'codeview']],
        ['help', ['help']],
    ],
    'js': (
        static_url('js/summernote-emoji-config.js'),
        static_url('components/summernote-emoji/tam-emoji/js/config.js'),
        static_url('components/summernote-emoji/tam-emoji/js/tam-emoji.min.js'),
    ),
    'css': (
        static_url('components/summernote-emoji/tam-emoji/css/emoji.css'),
        static_url('css/pyconkr.css'),
        static_url('css/pyconkr-summernote.css'),
    ),
}


# ACCOUNT_UNIQUE_EMAIL = False
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
        ]
    },
    # Didn't finish yet
    # https://django-allauth.readthedocs.io/en/latest/providers.html#facebook
    'facebook': {
        'METHOD': 'oauth2',
        # 'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}

SPEAKER_IMAGE_MAXIMUM_FILESIZE_IN_MB = 5
SPEAKER_IMAGE_MINIMUM_DIMENSION = (500, 500)

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'SLACK_TOKEN': ('', '홈페이지에서 파준위 슬랙으로 알림을 보내기 위한 토큰'),
    'TOTAL_TICKET': (1800, '판매할 전체 티켓 수량'),
    'IMP_DOM_USER_CODE': ('', '아임포트 국내용 유저 번호'),
    'IMP_DOM_API_KEY': ('', '아임포트 국내용 API KEY'),
    'IMP_DOM_API_SECRET': ('', '아임포트 국내용 API SECRET'),
    'IMP_INTL_USER_CODE': ('', '아임포트 해외용 유저 번호'),
    'IMP_INTL_API_KEY': ('', '아임포트 해외용 API KEY'),
    'IMP_INTL_API_SECRET': ('', '아임포트 해외용 API SECRET'),
    'SHOW_SLIDE_DATA': (False, 'Show slide data on schedule table and program detail'),
}

# For supporting i18n of django modules
MIGRATION_MODULES = {
    'flatpages': 'pyconkr.flatpages_migrations',
}
