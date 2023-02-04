from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$te!!n)yfa%$*^b7byf$3%_)4scf_@4o8&whn1^obh2c&_-nv#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #mis aplicaciones
    "autenticacion",
    "archivos",
    "gestion_archivos",

    #django rest framework
    'rest_framework',
    #aplicacion para importar y exportar archivos de excel
    'import_export',
    
    #drf filters
    'django_filters',

    #drf auth token
    'rest_framework.authtoken',
    'authemail',
    #cors
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'repositorioITSZ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'repositorioITSZ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#cambiar a base de datos postgresql_psycopg2 en produccion
#pip install psycopg2

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'POSTGRESQL_NAME',
        'USER': 'POSTGRESQL_USER',
        'PASSWORD': 'POSTGRESQL_PASS',
        'HOST':'POSTGRESQL_HOST',
        'PORT':'POSTGRESQL_PORT',
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
REST_FRAMEWORK = {
    #realizar filtros en las peticiones get
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
    #sistema de autenticacion por token
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    
    
    #custom docs
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    
    # paginacion default de rest
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 8,
    
}
AUTH_USER_MODEL = "autenticacion.CustomUser"

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'


# media root
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#campos para el registro con email
EMAIL_FROM ='336e567a0446fd'
EMAIL_BCC ='336e567a0446fd'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '336e567a0446fd'
EMAIL_HOST_PASSWORD = 'f5e98e01763afa'
EMAIL_PORT = '2525'


""" EMAIL_FROM ='186W0568@zongolica.tecnm.mx'
EMAIL_BCC ='186W0568@zongolica.tecnm.mx'

EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='186W0568@zongolica.tecnm.mx'
EMAIL_HOST_PASSWORD ='TRINIDAD@1806'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False """



#settings from corsheaders
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = ["https://3d7a-2806-10a6-16-85e8-79a6-669e-b0bf-1c6f.ngrok.io"]

# cambiar cada que se hagan pruebas externas para permitir el crf token
CSRF_TRUSTED_ORIGINS = ['https://3d7a-2806-10a6-16-85e8-79a6-669e-b0bf-1c6f.ngrok.io']
