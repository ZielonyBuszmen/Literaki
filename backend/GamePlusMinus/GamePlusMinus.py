import logging
import asyncio

from backend.messages import game_plus_minus_state

logging.basicConfig()


class GamePlusMinus:
    def __init__(self):
        self.game_counter = 0
        self.players = set()

    async def game(self, action):
        if action['action'] == 'minus':
            self.game_counter -= 1
            await self.notify_state()
        elif action['action'] == 'plus':
            self.game_counter += 1
            await self.notify_state()
        else:
            logging.error(
                "unsupported event: {}", action)

    async def notify_state(self):
        message = game_plus_minus_state(self.game_counter)
        await self.notify_all_players(message)

    def get_state(self):
        return game_plus_minus_state(self.game_counter)

    async def notify_all_players(self, message):
        if self.players:
            await asyncio.wait([player.send(message) for player in self.players])
