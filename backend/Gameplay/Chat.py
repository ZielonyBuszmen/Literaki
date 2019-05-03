import time

from backend import actions


class Chat:
    async def chat_it(self, sender, receiver, message: str):
        actual_time = time.time()
        sender_message = actions.send_chat_message(True, message, actual_time)
        opponent_message = actions.send_chat_message(False, message, actual_time)
        await sender.send(sender_message)
        await receiver.send(opponent_message)
