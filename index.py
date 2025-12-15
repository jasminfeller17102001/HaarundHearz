import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HaarundHaerz.settings')
django.setup()

from HaarundHaerz.wsgi import application

app = application