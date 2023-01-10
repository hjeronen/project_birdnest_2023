from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PilotListConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = 'pilot_list'
        self.room_group_name = 'pilot_list'

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, event):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def pilot_data(self, event):
        data = event["data"]

        await self.send(text_data=json.dumps({"data": data}))
