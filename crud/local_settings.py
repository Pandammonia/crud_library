from pathlib import Path
SECRET_KEY = 'django-insecure-#)7giwb(mlm^#b%co-!5d1-cb0i9h7a!u5g=02i4e=)p^u_p!1'
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}