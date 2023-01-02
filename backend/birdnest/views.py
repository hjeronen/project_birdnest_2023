from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PilotSerializer
from .models import Pilot

class PilotView(viewsets.ModelViewSet):
    serializer_class = PilotSerializer
    queryset = Pilot.objects.all()
