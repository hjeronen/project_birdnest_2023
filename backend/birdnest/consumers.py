from django.conf import settings
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
from django.core.asgi import get_asgi_application
import json

class PilotListConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'pilot_list'
        self.room_group_name = 'pilot_list'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, event):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
    
    # Receive message from WebSocket
    def receive(self, text_data):
        print('received some data')
        text_data_json = json.loads(text_data)
        data = text_data_json["data"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "new_ticks", "data": data}
        )

    # Receive message from room group
    def new_ticks(self, event):
        print('sending some data')
        print(event['data'])
        data = event["data"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"data": data}))

class PilotBroadcastingConsumer(WebsocketConsumer):

    def broadcast(self, event):
        while True:
            self.channel_layer.send(
                "pilot_list",
                {
                    "type": "new_ticks",
                    "data": "hello world",
                },
            )