import os
from dotmap import DotMap  # pip install dotmap
from dotenv import load_dotenv  # pip install python-dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'djangoOrm.insta',
    'django.contrib.auth',
    'django.contrib.contenttypes',
)

#load_dotenv('.env.dev')
load_dotenv('.env.prod')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'insta',
        'USER': 'root',
        'PASSWORD': 'docker123',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = 'S7wfj!ifd@sD&@eHW*QDwq)h8d(@jh09du@eh8q'

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'


