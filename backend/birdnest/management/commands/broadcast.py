from django.core.management.base import BaseCommand, CommandError
import json
from asgiref.sync import async_to_sync
import channels.layers
import requests
import xmltodict
import time
import numpy as np

class Command(BaseCommand):
    help = 'broadcast data'

    def handle(self, *args, **options):
        while True:
            response = requests.get('http://assignments.reaktor.com/birdnest/drones')
            print('response:')
            print(response)
            if response.status_code == 429:
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
                print(pilot)
                pilots.append(pilot)
            broadcast_ticks(pilots)
            time.sleep(2)

def broadcast_ticks(ticks):
        print('Broadcasting')
        print(ticks)
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.send)(
            'pilot_list', {
                "type": 'new_ticks',
                "data": json.dumps(ticks),
            })
        print(async_to_sync(channel_layer.receive)('pilot_list'))

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
    