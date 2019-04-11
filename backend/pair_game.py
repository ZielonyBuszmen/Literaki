import asyncio
import json
import websockets
from functools import partial

# aby wszystko dzialalo, ten plik musi byc klasa, a my musimy tworzyc nowe obiekty tej klasy, i kazdy obiekt bedzie gra, czy jakos tka
from websockets import WebSocketServerProtocol

from backend.GamePlusMinus import GamePlusMinus


class Gierka:
    def __init__(self):
        self.STATE = {'game_counter': 0}
        self.USERS = set()

    def state_event(self):
        return json.dumps({'type': 'GAME_PLUS_MINUS_STATE', **self.STATE})

    def users_event(self):
        return json.dumps({'type': 'NEW_PLAYER_CONNECTED', 'number_of_players': len(self.USERS)})

    async def notify_state(self):
        if self.USERS:  # asyncio.wait doesn't accept an empty list
            message = self.state_event()
            await asyncio.wait([user.send(message) for user in self.USERS])

    async def notify_users(self):
        if self.USERS:  # asyncio.wait doesn't accept an empty list
            message = self.users_event()
            await asyncio.wait([user.send(message) for user in self.USERS])

    async def register(self, websocket):
        self.USERS.add(websocket)
        await self.notify_users()

    async def unregister(self, websocket):
        self.USERS.remove(websocket)
        await self.notify_users()


# główna funkcja programu
async def pair_game(game_manager, websocket, path):
    await websocket.send(json.dumps({'type': 'rozpaczeto gre parowa,'}))
    await game_manager.register(websocket)
    try:
        await websocket.send(game_manager.state_event())
        async for message in websocket:
            data = json.loads(message)
            if data['action'] == 'minus':
                game_manager.STATE['game_counter'] -= 1
                await game_manager.notify_state()
            elif data['action'] == 'plus':
                game_manager.STATE['game_counter'] += 1
                await game_manager.notify_state()
    finally:
        await game_manager.unregister(websocket)


def start_pair_thread(port=6790):
    print("port dany do nowej gry ", port)

    gierka = Gierka()

    pair_game_with_arg = partial(
        pair_game,
        gierka  # argument game_manager
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(pair_game_with_arg, 'localhost', port))
    asyncio.get_event_loop().run_forever()
