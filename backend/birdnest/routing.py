from django.urls import path

from birdnest.consumers import PilotListConsumer

urlpatterns = [
    path("ws/pilot_list/", PilotListConsumer.as_asgi()),
]