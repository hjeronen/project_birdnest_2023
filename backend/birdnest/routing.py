from django.urls import path

from birdnest.consumers import PilotListConsumer

urlpatterns = [
    path("ws/backend/pilot_list/", PilotListConsumer.as_asgi()),
]