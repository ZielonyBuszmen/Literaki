import asyncio
import json
import websockets
from functools import partial

from websockets import WebSocketServerProtocol

from backend import actions


class GameManager:
    # tutaj musimy zrobic ustawianie gry - losowanie ble ble, kto zaczyna
    def __init__(self):
        self.password = self.castLostPassword()
        self.breaked = self.createNoBreakedPassword(self.password)
        self.actual_player = None
        self.players = set()

    # te hasło będzie losowane
    def castLostPassword(self):
        return {
            'category': 'Sypialnia',
            'saying': 'jak sobie pościelisz, tak się wyśpisz',
        }

    # będzie zwracało "zakreskowane" hasło
    def createNoBreakedPassword(self, password):
        return '___ _____ __________, ___ ___ _______'

    async def register(self, websocket):
        self.players.add(websocket)
        qty = len(self.players)
        await self.notify_all_players(actions.new_player_connected(qty))

    async def unregister(self, websocket):
        self.players.remove(websocket)
        qty = len(self.players)
        await self.notify_all_players(actions.player_disconnected(qty))

    async def notify_state(self):
        if self.players:  # asyncio.wait doesn't accept an empty list
            message = actions.send_game_state({
                'password': self.breaked,
            })
            await asyncio.wait([user.send(message) for user in self.players])

    async def react_for_action(self, websocket, action):
        type = action.type
        if type == actions.FE_SEND_LETTER and websocket == self.actual_player:
            self.player_send_letter(action.value)
        elif type == 'plus':
            pass
        else:
            print("unsupported action: {}", action)

    def player_send_letter(self, letter):
        if len(letter) == 1 and self.is_letter_in_password(letter):
            # jeśli jedna litera - spradzamy czy jest w haśle i je uzupełniamy
            self.fill_password(letter)
            pass
        elif self.is_proper_passord(letter):
            await self.notify_actual_player('wygrales')  # todo - poprawic message w obu funkcjach
            await self.notify_other_player('przegrales')
        else:
            self.change_player()  # zła odpowiedz, zmieniamy gracza
        self.notify_state()

    async def notify_actual_player(self, message):
        if self.actual_player:
            self.actual_player.send(message)

    async def notify_other_player(self, message):
        if self.actual_player:
            await asyncio.wait([player.send(message) for player in self.players if player != self.actual_player])

    async def notify_all_players(self, message):
        if self.players:
            await asyncio.wait([player.send(message) for player in self.players])

    async def change_player(self):  # zmienia gracza
        await self.notify_actual_player('koniec twojej tury')  # todo - poprawic message w obu funkcjach
        await self.notify_other_player('teraz twoja tura')
        self.actual_player = [player for player in self.players if player != self.actual_player][0]

    def is_letter_in_password(self, letter):
        pass  # todo - sprawdza czy litera jest w haśle

    def fill_password(self, letter):
        pass  # todo - uzupełnia literkę (lub literki, trzeba pomyśleć) w haśle

    def is_proper_passord(self, letters):
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
            game_manager.react_for_action(websocket, data)
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
