from channels.generic.websocket import AsyncJsonWebsocketConsumer


class RunningMateWebSocket(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content, **kwargs):
        pass

    async def send_json(self, content, **kwargs):
        await self.send_json(content)
