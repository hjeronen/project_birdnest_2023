from rest_framework import serializers
from birdnest.models import Pilot

class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = (
                'pilotId',
                'firstName',
                'lastName',
                'phoneNumber',
                'createdDt',
                'email',
                'closest_distance',
                'last_seen',
                'drone_serial_number'
            )
