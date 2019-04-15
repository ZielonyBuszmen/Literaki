import asyncio
import json
import websockets
from functools import partial

from websockets import WebSocketServerProtocol

from backend import actions
from backend.GamePlusMinus import game_helpers


class GameManager:
    # tutaj musimy zrobic ustawianie gry - losowanie ble ble, kto zaczyna
    def __init__(self):
        random_password = game_helpers.get_random_catchword()
        self.password = random_password['catchword']
        self.password_category = random_password['category']
        self.breaked = game_helpers.get_catchword_mock(self.password)
        self.actual_player = None
        self.players = set()

    # będzie zwracało "zakreskowane" hasło
    def createNoBreakedPassword(self, password):
        return '___ _____ __________, ___ ___ _______'

    async def register(self, websocket):
        self.players.add(websocket)
        qty = len(self.players)
        await self.notify_all_players(actions.new_player_connected(qty))
        if self.actual_player is None:
            self.actual_player = websocket

    async def unregister(self, websocket):
        self.players.remove(websocket)
        qty = len(self.players)
        await self.notify_all_players(actions.player_disconnected(qty))

    async def notify_state(self):
        if self.players:  # asyncio.wait doesn't accept an empty list
            message = actions.send_game_state({
                'password': self.breaked,
                'category': self.password_category,
            })
            await asyncio.wait([user.send(message) for user in self.players])

    async def react_for_action(self, websocket, action):
        type = action["type"]
        if type == actions.FE_SEND_LETTER and websocket == self.actual_player:
            await self.player_send_letter(action["value"])
        elif websocket != self.actual_player:
            await self.notify_other_player(actions.not_your_turn())
        else:
            print("unsupported action", action)
            await self.notify_other_player(actions.unsupported_action())

    async def player_send_letter(self, letter):
        if len(letter) == 1 and self.is_letter_in_password(letter):
            self.fill_password(letter)
        elif self.is_proper_password(letter):
            await self.notify_actual_player(actions.player_win_game())
            await self.notify_other_player(actions.player_lose_game())
        else:
            await self.change_player()
        await self.notify_state()

    async def notify_actual_player(self, message):
        if self.actual_player:
            await self.actual_player.send(message)

    async def notify_other_player(self, message):
        if self.actual_player:
            await asyncio.wait([player.send(message) for player in self.players if player != self.actual_player])

    async def notify_all_players(self, message):
        if self.players:
            await asyncio.wait([player.send(message) for player in self.players])

    async def change_player(self):  # zmienia gracza
        await self.notify_actual_player(actions.player_end_turn())
        await self.notify_other_player(actions.player_start_turn())
        self.actual_player = [player for player in self.players if player != self.actual_player][0]

    def is_letter_in_password(self, letter):
        return letter in self.password

    def fill_password(self, letter):
        index = 0
        for password_letter in self.password:
            if password_letter == letter:
                self.breaked = self.breaked[:index] + letter + self.breaked[index + 1:]
            index += 1

    def is_proper_password(self, letters):
        pass  # todo - sprawdza, czy całe hasło jest poprawne



# class Gierka:
#     def __init__(self):
#         self.STATE = {'game_counter': 0}
#         self.USERS = set()
#
#     def state_event(self):
#         return json.dumps({'type': 'BE_GAME_PLUS_MINUS_STATE', **self.STATE})
#
#     def users_event(self):
#         return json.dumps({'type': 'BE_NEW_PLAYER_CONNECTED', 'number_of_players': len(self.USERS)})
#
#     async def notify_state(self):
#         if self.USERS:  # asyncio.wait doesn't accept an empty list
#             message = self.state_event()
#             await asyncio.wait([user.send(message) for user in self.USERS])
#
#     async def notify_users(self):
#         if self.USERS:  # asyncio.wait doesn't accept an empty list
#             message = self.users_event()
#             await asyncio.wait([user.send(message) for user in self.USERS])
#
#     async def register(self, websocket):
#         self.USERS.add(websocket)
#         await self.notify_users()
#
#     async def unregister(self, websocket):
#         self.USERS.remove(websocket)
#         await self.notify_users()


# główna funkcja programu
async def game_websocket(game_manager, websocket, path):
    await websocket.send(actions.game_was_started())
    await game_manager.register(websocket)
    try:
        await game_manager.notify_state()
        async for message in websocket:
            data = json.loads(message)
            await game_manager.react_for_action(websocket, data)
    finally:
        await game_manager.unregister(websocket)


def start_pair_thread(port=6790):
    print("new port was created - ", port)

    game_manager = GameManager()

    pair_game_with_arg = partial(
        game_websocket,
        game_manager  # argument game_manager
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(pair_game_with_arg, 'localhost', port))
    asyncio.get_event_loop().run_forever()
