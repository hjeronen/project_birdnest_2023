from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class PilotListConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'pilot_list'
        self.room_group_name = 'pilot_list'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def pilot_data(self, event):
        data = event["data"]

        self.send(text_data=json.dumps({"data": data}))
