import asyncio
import websockets

from backend.Lobby.Lobby import Lobby
from backend.consts import START_PORT, SERVER

print("Server was started")

lobby = Lobby()


async def main(websocket, path: str):
    await lobby.register_new_player(websocket)
    try:
        async for message in websocket:
            pass
    finally:
        await lobby.unregister_player(websocket)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(main, SERVER, START_PORT))
asyncio.get_event_loop().run_forever()

print("Server was shut down")
