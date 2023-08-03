# 운영 환경을 의미하는 production의 약자 prod

import environ
from .base import *

ALLOWED_HOSTS = ["43.202.137.102"]
STATIC_ROOT = BASE_DIR / "static/"
STATICFILES_DIRS = []
DEBUG = False

env = environ.Env()
environ.Env.read_env(BASE_DIR/".env")

DATABASES = {
    "default":{
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": "5432",
    }
}
