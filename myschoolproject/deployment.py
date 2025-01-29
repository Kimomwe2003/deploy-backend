import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
# CSRF_TRUSTED_ORIGINS = ['https://'+os.environ('RENDER_EXTERNAL_HOSTNAME')]

# ALLOWED_HOSTS = ["*"]
# CSRF_TRUSTED_ORIGINS = ['https://deploy-backend-8r15.onrender.com']

ALLOWED_HOSTS = ['deploy-backend-8r15.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://deploy-backend-8r15.onrender.com']


DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware"
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]


CORS_ALLOWED_ORIGINS = [
    # "http://localhost:3000",  
    # "http://127.0.0.1:3000",
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTION_STRING']
# CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': CONNECTION_STR['dbname'], 
#         'HOST': CONNECTION_STR['host'], 
#         'USER': CONNECTION_STR['user'],
#         'PASSWORD': CONNECTION_STR['password'],
        
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default = os.environ['DATABASE_URL'],
        conn_max_age = 600,
    )
}

STATIC_ROOT =  BASE_DIR / 'staticfiles'


