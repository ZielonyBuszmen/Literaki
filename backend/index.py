# globalne bibliteki
import asyncio
import json
import websockets
import threading

# lokalne importy klas
from backend.Players.PlayersManager import PlayersManager
from backend.GamePlusMinus.GamePlusMinus import GamePlusMinus
from backend.pair_game import start_pair_thread

print("Serwer został uruchomiony")


class PortManager:
    def __init__(self):
        self.port = 6790

    def getPort(self):
        self.port += 1
        return self.port


players_manager = PlayersManager()
game = GamePlusMinus(players_manager)
port_manager = PortManager()

port_to_new_game = 6790


# główna funkcja programu
async def counter(websocket, path):
    await players_manager.register_new_player(websocket)
    try:
        await websocket.send(game.get_state())
        async for message in websocket:
            action = json.loads(message)
    finally:
        await players_manager.unregister_player(websocket)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(counter, 'localhost', 6789))
asyncio.get_event_loop().run_forever()
