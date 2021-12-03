from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        # Connect users to a open chat
        self.recipient_username = self.scope['url_route']['kwargs']['username']

        await self.channel_layer.group_add(self.recipient_username, self.channel_name)
        await self.accept()
        print(f"Connected to room {self.recipient_username}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.recipient_username, self.channel_name)
        print(f"Disconnected {self.recipient_username}")
