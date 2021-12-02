from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        # Connect users to a open chat
        await self.channel_layer.group_add("chat", self.channel_name)
        await self.accept()
        print("Connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat", self.channel_name)
        print(f"Disconnected")
