from settings import BASE_DIR

STATIC_URL = BASE_DIR + '/static/'
TEMPLATES_DIR = BASE_DIR + '/templates/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'jeffrey',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
