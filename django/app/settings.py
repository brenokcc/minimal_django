import os
from pathlib import Path
from minio import Minio

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

SECRET_KEY = 'secret-key'
DEBUG = True
ROOT_URLCONF = 'app.urls'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ["storages", "app"]
MIDDLEWARE = []

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db",
        "USER": "user",
        "PASSWORD": "123",
        "HOST": "postgres",
        "PORT": 5432,
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

AWS_S3_ACCESS_KEY_ID = "user"
AWS_S3_SECRET_ACCESS_KEY = "12345678"
AWS_S3_ENDPOINT_URL = "http://host.docker.internal:9000"
#AWS_QUERYSTRING_AUTH = True
#AWS_QUERYSTRING_EXPIRE = 300
#AWS_S3_URL_PROTOCOL = 'http:'
# AWS_S3_CUSTOM_DOMAIN = 'host.docker.internal:9000'
#AWS_S3_REGION_NAME = 'us-east-2'
#AWS_S3_SIGNATURE_VERSION = 's3v4'
#AWS_ACCESS_KEY_ID = "user"
#AWS_SECRET_ACCESS_KEY = "12345678"
AWS_STORAGE_BUCKET_NAME = 'app'
#AWS_DEFAULT_ACL = 'public-read'

minio_client = Minio(AWS_S3_ENDPOINT_URL.replace('http://', ''), access_key=AWS_S3_ACCESS_KEY_ID, secret_key=AWS_S3_SECRET_ACCESS_KEY, secure=False)
if not minio_client.bucket_exists(AWS_STORAGE_BUCKET_NAME):
    minio_client.make_bucket(AWS_STORAGE_BUCKET_NAME)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Check if running in a production environment
STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {
            # 'bucket_name': AWS_STORAGE_BUCKET_NAME,
            #'region_name': 'us-east-2',
            #'default_acl': 'public-read',
            #'file_overwrite': True,
            #'custom_domain': 'localhost:9000',
        },
    },
    'staticfiles': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
        'OPTIONS': {
            'location': STATIC_ROOT,
        },
    }
}

