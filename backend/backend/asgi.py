"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from birdnest.consumers import PilotListConsumer

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings_dev')

# set settings file to use
use_prod_settings = os.environ.get('DJANGO_PRODUCTION', 'false')
if use_prod_settings == 'false':
    print('Using development settings.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings_dev')
else:
    print('Using production settings.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django_asgi_application = get_asgi_application()

import birdnest.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_application,
        "websocket": URLRouter(birdnest.routing.urlpatterns),
        "channel": ChannelNameRouter(
            {
                "pilot_list": PilotListConsumer.as_asgi(),
            }
        ),
    }
)
