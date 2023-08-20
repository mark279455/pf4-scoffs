import os
from django.conf import settings

def exists(file):
    if os.path.exists(file):
        print(f"exists {file}")
    else:
        print(f"MOT EXISTS {file}")



exists('static/css/base.css')

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

exists('main/settings.py')

print(f"settings.STATICFILES_DIRS = {settings.STATICFILES_DIRS}")

print(f"settings.STATICFILES_DIRS = {getattr(settings, 'STATICFILES_DIRS', None)}")


