import asyncio

from backend import actions
from backend.Gameplay import game_helpers


class GameplayManager:
    def __init__(self):
        random_password = game_helpers.get_random_catchword()
        self.password = random_password['catchword']
        self.password_category = random_password['category']
        self.broke = game_helpers.get_catchword_mock(self.password)
        self.actual_player = None
        self.players_moves = 0
        self.players = set()

    async def register(self, websocket):
        self.players.add(websocket)
        qty = len(self.players)
        await self.notify_all_players(actions.new_player_connected(qty))
        if self.actual_player is None:
            self.actual_player = websocket
            await self.notify_actual_player(actions.player_start_turn())

    async def unregister(self, websocket):
        self.players.remove(websocket)
        qty = len(self.players)
        await self.notify_all_players(actions.player_disconnected(qty))

    async def notify_state(self):
        if self.players:
            message = actions.send_game_state(self.broke, self.password_category)
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
            if self.is_catchword_filled():
                await self.notify_actual_player(actions.player_win_game())
                await self.notify_other_player(actions.player_lose_game())
        elif self.is_proper_catchword(letter):
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
        self.players_moves += 1
        await self.notify_actual_player(actions.player_end_turn())
        await self.notify_other_player(actions.player_start_turn())
        self.actual_player = [player for player in self.players if player != self.actual_player][0]
        round_number = int(self.players_moves / 2) + 1
        await self.notify_all_players(actions.round_number(round_number))

    def is_letter_in_password(self, letter):
        return letter in self.password

    def fill_password(self, letter):
        index = 0
        for password_letter in self.password:
            if password_letter == letter:
                self.broke = self.broke[:index] + letter + self.broke[index + 1:]
            index += 1

    def is_proper_catchword(self, letters):
        return self.password.lower() == letters.lower()

    def is_catchword_filled(self):
        return self.password == self.broke
