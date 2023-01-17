from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from asgiref.sync import async_to_sync
import channels.layers

from birdnest.models import Pilot
from birdnest.serializers import PilotSerializer
from birdnest.drone_control import get_violating_drones, get_distance

from datetime import datetime, timedelta

import requests
import xmltodict
import time
import xmltodict
import requests

class Command(BaseCommand):
    help = 'broadcast pilot data'

    def handle(self, *args, **options):
        print('Broadcasting')
        while True:
            try:
                response = requests.get('http://assignments.reaktor.com/birdnest/drones')
                if response.status_code != 200:
                    print('error: ' + str(response.status_code))
                    time.sleep(10)
                    continue

                response_as_dict = xmltodict.parse(response.text)
                drones = get_violating_drones(response_as_dict)
                pilots = get_pilots(drones)

                update_pilot_list(pilots)

                pilot_list = list(Pilot.objects.all())
                serializer = PilotSerializer(pilot_list, many=True)

                broadcast_pilots(serializer.data)

            except:
                print('An error occurred.')

            time.sleep(10)


def get_pilots(drones):
    pilots = []
    for drone in drones:
        res = requests.get(
            'http://assignments.reaktor.com/birdnest/pilots/%s' % drone['serialNumber']
            )
        pilot = res.json()

        if 'error' in pilot:
            print('error: ' + pilot['error'])
            continue

        distance = get_distance(drone)

        pilot['closest_distance'] = distance
        pilot['last_seen'] = make_aware(datetime.now())
        pilot['drone_serial_number'] = drone['serialNumber']

        pilots.append(pilot)

    return pilots

def broadcast_pilots(pilots):
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'pilot_list', {
            "type": 'pilot_data',
            "data": pilots
        })

def update_pilot_list(pilots):
    for pilot in pilots:
        db_pilot = Pilot.objects.filter(pilotId=pilot['pilotId'])
        if db_pilot:
            db_pilot.update(last_seen=make_aware(datetime.now()),
                            closest_distance=min(
                                db_pilot[0].closest_distance,
                                pilot['closest_distance']
                            ))
            continue

        Pilot.objects.create(**pilot)

    Pilot.objects.filter(last_seen__lt=make_aware(datetime.now() - timedelta(minutes=10))).delete()
    