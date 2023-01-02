from rest_framework import serializers
from .models import Pilot

class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ('pilotId', 'firstName', 'lastName', 'phoneNumber', 'createdDt', 'email')
