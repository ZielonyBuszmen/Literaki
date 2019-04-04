import asyncio
import threading
import json

from backend.pair_game import start_pair_thread
from .Player import Player
from backend.messages import new_player_connected, player_disconnected


class PlayersManager:
    def __init__(self):
        self.players = []
        self.port = 6790

    async def register_new_player(self, websocket):
        player = Player(websocket, "Bez nazwy")
        self.players.append(player)
        message = new_player_connected(self.count_players())
        await self.notify_players(message)
        await self.create_new_thread()

    async def create_new_thread(self):
        if len(self.players) == 2:
            first = self.players.pop(0)
            second = self.players.pop(0)

            port = self.port
            self.port += 1

            thread = threading.Thread(target=start_pair_thread,
                                      args=(port,))
            await first.get_websocket().send(json.dumps({'type': 'NEW_THREAD_WAS_OPENED_TO_YOU', 'port': port}))
            await second.get_websocket().send(json.dumps({'type': 'NEW_THREAD_WAS_OPENED_TO_YOU', 'port': port}))

            thread.start()
        else:
            await self.players[0].get_websocket().send(json.dumps({'type': 'WAITING_FOR_SECOND_PLAYER'}))

    async def unregister_player(self, websocket):
        # delete player with websocket from array
        self.players = [player for player in self.players if player.get_websocket() != websocket]
        message = player_disconnected(self.count_players())
        await self.notify_players(message)

    async def notify_players(self, message):
        if self.players:  # asyncio.wait nie akceptuje pustej listy
            await asyncio.wait([self.sendTo(player, message) for player in self.players])

    def count_players(self):
        return len(self.players)

    def getAllPlayers(self):
        return self.players

    def sendTo(self, player, message):
        return player.get_websocket().send(message)
