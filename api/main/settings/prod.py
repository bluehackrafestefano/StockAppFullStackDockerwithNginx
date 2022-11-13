from decouple import config

from main.settings.base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE


DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_NAME"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

STATIC_ROOT = BASE_DIR / 'static/'

THIRD_PARTY_APPS = [
    "corsheaders",
]

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

CORS_ALLOW_ALL_ORIGINS = True
