from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PilotSerializer
from .models import Pilot
import xmltodict
import pprint
import json
import requests
import numpy as np
from datetime import datetime, timedelta

class PilotView(viewsets.ModelViewSet):
    serializer_class = PilotSerializer
    queryset = Pilot.objects.all()

    def list(self, request, *args, **kwargs):
        response = requests.get('http://assignments.reaktor.com/birdnest/drones')
        response_as_dict = xmltodict.parse(response.text)
        drones = get_violating_drones(response_as_dict)
        pilots = []
        for drone in drones:
            res = requests.get('http://assignments.reaktor.com/birdnest/pilots/%s' % drone['serialNumber'])
            res = res.json()
            db_pilot = Pilot.objects.filter(pilotId=res['pilotId'])
            if db_pilot:
                db_pilot.update(last_seen=datetime.now())
                continue
            pilot = Pilot.objects.create(**res)
            pilots.append(pilot)
        Pilot.objects.filter(last_seen__lt=datetime.now() - timedelta(minutes=10)).delete()

        queryset = self.get_queryset()
        serializer = PilotSerializer(queryset, many=True)
        return Response(serializer.data)
        

def get_violating_drones(data):
    drones = data['report']['capture']['drone']
    violating = []
    for drone in drones:
        if check_distance(get_distance(drone)):
            violating.append(drone)
    return violating

def check_distance(distance):
    limit = 100000
    return distance < limit

def get_distance(drone):
    origo = 250000

    a = (origo - float(drone['positionY']))**2
    b = (origo - float(drone['positionX']))**2
    c = np.sqrt(a + b)

    return c
