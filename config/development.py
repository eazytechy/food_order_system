from config.common import *
import os

ENV = "DEVELOPMENT"
DEBUG = True


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev_database',
        'USER': 'et_dev_user',
        'PASSWORD': 'et@user@123',
        "HOST": "127.0.0.1",
        'TIME_ZONE': 'Asia/Kolkata'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'



