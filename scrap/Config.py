import environ  # pip install django-environ
from dotmap import DotMap  # pip install dotmap


class Config:

    def __init__(self):
        env = environ.Env(DEBUG=(bool, True))
        environ.Env.read_env(
            env_file='.env'
        )
        self.MOBILE_IP = env('MOBILE_IP')
        self.INNER_IP = env('INNER_IP')
        self.WIFI_IP = env('WIFI_IP')
