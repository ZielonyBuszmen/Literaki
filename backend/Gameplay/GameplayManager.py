import asyncio

from backend import actions
from backend.Gameplay.Catchword import Catchword
from backend.Gameplay.Chat import Chat


class GameplayManager:
    def __init__(self):
        self.catchword = Catchword()
        self.actual_player = None
        self.players_moves = 0
        self.players = set()
        self.chat = Chat()

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
        await self.__notify_all_players(actions.player_disconnected_from_gameplay(qty))

    async def notify_state(self):
        if self.players:
            message = actions.send_game_state(self.catchword.get_broke(), self.catchword.get_category())
            await asyncio.wait([user.send(message) for user in self.players])

    async def react_for_action(self, websocket, action: dict):
        if len(self.players) < 2:
            return
        type = action["type"]
        if type == actions.FE_SEND_LETTER and websocket == self.actual_player:
            letter = action["value"].lower()
            await self.__player_send_letter(letter)
        elif type == actions.FE_SEND_CHAT_MESSAGE:
            second_player = self.__get_second_player(websocket)
            await self.chat.chat_it(websocket, second_player, action["value"])
        elif websocket != self.actual_player:
            await self.__notify_other_player(actions.not_your_turn())
        else:
            print("unsupported action", action)
            await websocket.send(actions.unsupported_action())

    async def __player_send_letter(self, letter: str):
        if len(letter) == 1 and self.catchword.is_letter_in(letter):
            self.catchword.fill_catchword(letter)
            if self.catchword.is_catchword_filled():
                await self.__notify_actual_player(actions.player_win_game())
                await self.__notify_other_player(actions.player_lose_game())
        elif self.catchword.is_correct_catchword(letter):
            self.catchword.set_broke()
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

    def __get_second_player(self, current_player):
        return [player for player in self.players if player != current_player][0]
