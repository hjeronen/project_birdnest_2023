"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# set settings file to use
use_prod_settings = os.environ.get('DJANGO_PRODUCTION', 'false')
if use_prod_settings == 'false':
    print('Using development settings.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings_dev')
else:
    print('Using production settings.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
