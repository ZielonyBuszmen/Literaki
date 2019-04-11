import asyncio
import threading

from backend.consts import PORT_TO_NEW_GAME
from backend.pair_game import start_pair_thread
from backend.actions import new_player_connected, player_disconnected, new_thread_was_opened, waiting_for_second_player


class Lobby:
    def __init__(self):
        self.players = []
        self.port = PORT_TO_NEW_GAME

    async def register_new_player(self, websocket):
        self.players.append(websocket)
        message = new_player_connected(self.count_players())
        await self.notify_all_players(message)

        if self.count_players() == 2:
            await self.create_new_game()
        else:
            await self.notify_all_players(waiting_for_second_player())

    async def create_new_game(self):
        first_player = self.players.pop(0)
        second_player = self.players.pop(0)

        port = self.get_increased_port()

        thread = threading.Thread(target=start_pair_thread, args=(port,))
        thread.start()
        await first_player.send(new_thread_was_opened(port))
        await second_player.send(new_thread_was_opened(port))

    async def unregister_player(self, websocket):
        self.players.remove(websocket)
        message = player_disconnected(self.count_players())
        await self.notify_all_players(message)

    async def notify_all_players(self, message):
        if self.players:
            await asyncio.wait([player.send(message) for player in self.players])

    def count_players(self):
        return len(self.players)

    def get_increased_port(self):
        self.port += 1
        return self.port
