import asyncio

from .Player import Player
from backend.messages import new_player_connected, player_disconnected


class PlayersManager:
    def __init__(self):
        self.players = []

    async def register_new_player(self, websocket):
        player = Player(websocket, "Bez nazwy")
        self.players.append(player)
        message = new_player_connected(self.count_players())
        await self.notify_players(message)

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

    def sendTo(self, player, message):
        return player.get_websocket().send(message)
