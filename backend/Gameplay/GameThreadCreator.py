import asyncio
import json
import websockets

from backend import actions
from backend.consts import SERVER


class GameThreadCreator:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    async def game_websocket(self, websocket, path):
        await websocket.send(actions.game_was_started())
        await self.game_manager.register(websocket)
        try:
            await self.game_manager.notify_state()
            async for message in websocket:
                data = json.loads(message)
                await self.game_manager.react_for_action(websocket, data)
        finally:
            await self.game_manager.unregister(websocket)

    def start_new_game_thread(self, port=6790):
        print("new port was created - ", port)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            websockets.serve(self.game_websocket, SERVER, port))
        loop.run_forever()
