# globalne bibliteki
import asyncio
import json
import websockets

# lokalne importy klas
from backend.Players.PlayersManager import PlayersManager
from backend.GamePlusMinus.GamePlusMinus import GamePlusMinus

print("Serwer został uruchomiony")

players_manager = PlayersManager()
game = GamePlusMinus(players_manager)


# główna funkcja programu
async def counter(websocket, path):
    await players_manager.register_new_player(websocket)
    try:
        await websocket.send(game.get_state())
        async for message in websocket:
            action = json.loads(message)
            await game.game(action)
    finally:
        await players_manager.unregister_player(websocket)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(counter, 'localhost', 6789))
asyncio.get_event_loop().run_forever()
