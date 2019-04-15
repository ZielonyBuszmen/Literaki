import logging
import asyncio

from backend.actions import game_plus_minus_state, FE_SEND_LETTER

logging.basicConfig()

# to jest do wywalenia
#
# class GameLoop:
#     def __init__(self):
#         self.game_counter = 0
#         self.players = set()
#
#     async def game_loop(self, action):
#         type = action.type
#         if type == FE_SEND_LETTER:
#             self.game_counter -= 1
#             await self.notify_state()
#         elif type == 'plus':
#             self.game_counter += 1
#             await self.notify_state()
#         else:
#             print("unsupported event: {}", action)
#
#     async def notify_state(self):
#         message = game_plus_minus_state(self.game_counter)
#         await self.notify_all_players(message)
#
#     def get_state(self):
#         return game_plus_minus_state(self.game_counter)
#
#     async def notify_all_players(self, message):
#         if self.players:
#             await asyncio.wait([player.send(message) for player in self.players])
