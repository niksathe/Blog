import os


from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ygb9%9m4e+r=3q=t!+c0y2%=$c^8k_j8dzxt#2+b3k!tqwe#p&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','139.59.26.57','142.93.214.141']


# Application definition

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Authentication:
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #newslater
    'sorl.thumbnail',
    'newsletter',
    #system
    'post',
    #editor
    'ckeditor',
    'ckeditor_uploader',
    'tinymce',
    'crispy_forms',

    #social accounts
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

SITE_ID = 1

NEWSLETTER_RICHTEXT_WIDGET = 'tinymce.widgets.TinyMCE'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thenetworklegal@gmail.com'
EMAIL_HOST_PASSWORD = 'Legal@8118.'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = '/user'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True

CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thenl.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'thenl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

'''if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'thenl',
        'USER': 'thenl',
        'PASSWORD': 'thenl8118',
        'HOST': 'localhost',
        'PORT': '',
        }
    }'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('ar', _('Arabic')),
    ('az', _('Azerbaijani')),
    ('bg', _('Bulgarian')),
    ('bn', _('Bengali')),
    ('ca', _('Catalan')),
    ('cs', _('Czech')),
    ('da', _('Danish')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('et', _('Estonian')),
    ('fa', _('Persian')),
    ('fr', _('French')),
    ('hi', _('Hindi')),
    ('hu', _('Hungarian')),
    ('hy', _('Armenian')),
    ('id', _('Indonesian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('mn', _('Mongolian')),
    ('nb', _('Norwegian')),
    ('nl', _('Dutch')),
    ('pl', _('Polish')),
    ('pt', _('Portuguese')),
    ('pt-br', _('Brazilian Portuguese')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('sr', _('Serbian')),
    ('sw', _('Swahili')),
    ('sv', _('Swedish')),
    ('th', _('Thai')),
    ('tr', _('Turkish')),
    ('uk', _('Ukrainian')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese'))]


LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
USE_I18N = True
USE_L10N = True
USE_TZ = True

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

'''STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')'''
