import asyncio
import time

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
        await self.__notify_all_players(actions.new_player_connected(qty))
        if self.actual_player is None:
            self.actual_player = websocket
            await self.__notify_actual_player(actions.player_start_turn())

    async def unregister(self, websocket):
        self.players.remove(websocket)
        qty = len(self.players)
        await self.__notify_all_players(actions.player_disconnected(qty))

    async def notify_state(self):
        if self.players:
            message = actions.send_game_state(self.broke, self.password_category)
            await asyncio.wait([user.send(message) for user in self.players])

    async def react_for_action(self, websocket, action: dict):
        type = action["type"]
        if type == actions.FE_SEND_LETTER and websocket == self.actual_player:
            letter = action["value"].lower()
            await self.__player_send_letter(letter)
        elif type == actions.FE_SEND_CHAT_MESSAGE:
            await self.__chat_it(websocket, action["value"])
        elif websocket != self.actual_player:
            await self.__notify_other_player(actions.not_your_turn())
        else:
            print("unsupported action", action)
            await websocket.send(actions.unsupported_action())

    async def __player_send_letter(self, letter: str):
        if len(letter) == 1 and self.__is_letter_in_password(letter):
            self.__fill_password(letter)
            if self.__is_catchword_filled():
                await self.__notify_actual_player(actions.player_win_game())
                await self.__notify_other_player(actions.player_lose_game())
        elif self.__is_proper_catchword(letter):
            self.broke = letter
            await self.__notify_actual_player(actions.player_win_game())
            await self.__notify_other_player(actions.player_lose_game())
        else:
            await self.__change_player()
        await self.notify_state()

    async def __notify_actual_player(self, message: str):
        if self.actual_player:
            await self.actual_player.send(message)

    async def __notify_other_player(self, message: str):
        if self.actual_player:
            await asyncio.wait([player.send(message) for player in self.players if player != self.actual_player])

    async def __notify_all_players(self, message: str):
        if self.players:
            await asyncio.wait([player.send(message) for player in self.players])

    async def __change_player(self):
        self.players_moves += 1
        await self.__notify_actual_player(actions.player_end_turn())
        await self.__notify_other_player(actions.player_start_turn())
        self.actual_player = [player for player in self.players if player != self.actual_player][0]
        round_number = int(self.players_moves / 2) + 1
        await self.__notify_all_players(actions.round_number(round_number))

    def __is_letter_in_password(self, letter: str) -> bool:
        return letter in self.password

    def __fill_password(self, letter: str) -> None:
        index = 0
        for password_letter in self.password:
            if password_letter == letter:
                self.broke = self.broke[:index] + letter + self.broke[index + 1:]
            index += 1

    def __is_proper_catchword(self, letters: str) -> bool:
        return self.password.lower() == letters.lower()

    def __is_catchword_filled(self) -> bool:
        return self.password == self.broke

    async def __chat_it(self, websocket, message: str):
        actual_time = time.time()
        sender_message = actions.send_chat_message(True, message, actual_time)
        opponent_message = actions.send_chat_message(False, message, actual_time)
        await websocket.send(sender_message)
        await asyncio.wait([player.send(opponent_message) for player in self.players if player != websocket])
