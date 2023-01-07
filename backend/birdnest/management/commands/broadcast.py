from django.core.management.base import BaseCommand, CommandError
import json
from asgiref.sync import async_to_sync
import channels.layers
import requests
import xmltodict
import time
import numpy as np
from birdnest.models import Pilot
import xmltodict
import requests
from datetime import datetime, timedelta
from birdnest.serializers import PilotSerializer

class Command(BaseCommand):
    help = 'broadcast data'

    def handle(self, *args, **options):
        while True:
            response = requests.get('http://assignments.reaktor.com/birdnest/drones')
            # print('response:')
            # print(response)
            if response.status_code != 200:
                print('error, new loop')
                time.sleep(2)
                continue
            response_as_dict = xmltodict.parse(response.text)
            drones = get_violating_drones(response_as_dict)
            pilots = []
            for drone in drones:
                res = requests.get('http://assignments.reaktor.com/birdnest/pilots/%s' % drone['serialNumber'])
                pilot = res.json()
                if 'error' in pilot:
                    print('got error')
                    continue
                # print(pilot)
                distance = get_distance(drone)
                pilot['closest_distance'] = distance
                pilots.append(pilot)
            update_pilot_list(pilots)
            pilot_list = list(Pilot.objects.all())
            serializer = PilotSerializer(pilot_list, many=True)
            # print('pilot_list')
            # print(serializer.data)
            broadcast_ticks(serializer.data)
            time.sleep(2)

def broadcast_ticks(ticks):
        print('Broadcasting')
        # print(ticks)
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'pilot_list', {
                "type": 'new_ticks',
                "data": json.dumps(ticks)
            })

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

def update_pilot_list(pilots):
    for pilot in pilots:
        db_pilot = Pilot.objects.filter(pilotId=pilot['pilotId'])
        if db_pilot:
            old_distance = db_pilot[0].closest_distance
            print(old_distance)
            new_distance = pilot['closest_distance']
            print(new_distance)
            db_pilot.update(last_seen=datetime.now(), closest_distance=min(old_distance, new_distance))
            continue
        new_pilot = Pilot.objects.create(**pilot)
    Pilot.objects.filter(last_seen__lt=datetime.now() - timedelta(minutes=10)).delete()
    