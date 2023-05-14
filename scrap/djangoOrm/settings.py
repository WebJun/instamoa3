import os
import environ  # pip install django-environ
from dotmap import DotMap  # pip install dotmap
from dotenv import load_dotenv  # pip install python-dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = environ.Env(DEBUG=(bool, True))

isDev = False
envPath = os.path.join(f'{BASE_DIR}/', '.prod.env')

if str(BASE_DIR) == '/scrap/djangoOrm':
    isDev = True

if isDev:
    envPath = os.path.join(f'{BASE_DIR}/', '.dev.env')

environ.Env.read_env(
    env_file=envPath
)

INSTALLED_APPS = (
    'djangoOrm.insta',
    'django.contrib.auth',
    'django.contrib.contenttypes',
)

# load_dotenv('.env.dev')
load_dotenv('.env.prod')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_DATABASE'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4'  # 중요 우분투에서 필요
        }
    }
}
# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = env('SECRET_KEY')

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
