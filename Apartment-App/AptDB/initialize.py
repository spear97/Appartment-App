import os
import django


def init():
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AptDB.settings')

    # Configure Django settings
    django.setup()
