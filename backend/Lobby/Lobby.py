import asyncio
import threading

from backend.Gameplay.GameplayManager import GameplayManager
from backend.Gameplay.GameThreadCreator import GameThreadCreator
from backend.consts import PORT_TO_NEW_GAME
from backend.actions import new_player_connected, player_disconnected, new_thread_was_opened, waiting_for_second_player


class Lobby:
    def __init__(self):
        self.players = []
        self.port = PORT_TO_NEW_GAME

    async def register_new_player(self, websocket):
        self.players.append(websocket)
        message = new_player_connected(self.__count_players())
        await self.__notify_all_players(message)

        if self.__count_players() == 2:
            await self.__create_new_game()
        else:
            await self.__notify_all_players(waiting_for_second_player())

    async def unregister_player(self, websocket):
        if websocket in self.players:
            self.players.remove(websocket)
        message = player_disconnected(self.__count_players())
        await self.__notify_all_players(message)

    async def __create_new_game(self):
        first_player = self.players.pop(0)
        second_player = self.players.pop(0)

        port = self.__get_increased_port()

        gameplay_manager = GameplayManager()
        thread_creator = GameThreadCreator(gameplay_manager)

        thread = threading.Thread(target=thread_creator.start_new_game_thread, args=(port,))
        thread.start()
        await first_player.send(new_thread_was_opened(port))
        await second_player.send(new_thread_was_opened(port))

    async def __notify_all_players(self, message: str):
        if self.players:
            await asyncio.wait([player.send(message) for player in self.players])

    def __count_players(self) -> int:
        return len(self.players)

    def __get_increased_port(self) -> int:
        self.port += 1
        return self.port
