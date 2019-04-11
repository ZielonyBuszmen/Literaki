# Lista message, które będą przesyłane przez websocket
# message zaczynające się na BE_ pochodzą z serwera (backendu)
# message zaczynające się na FE_ pochodzą od klienta (frontendu)

import json

BE_NEW_PLAYER_CONNECTED = 'BE_NEW_PLAYER_CONNECTED'
BE_PLAYER_DISCONNECTED = 'BE_PLAYER_DISCONNECTED'
BE_GAME_PLUS_MINUS_STATE = 'BE_GAME_PLUS_MINUS_STATE'
BE_NEW_THREAD_WAS_OPENED_TO_YOU = 'BE_NEW_THREAD_WAS_OPENED_TO_YOU'
BE_WAITING_FOR_SECOND_PLAYER = 'BE_WAITING_FOR_SECOND_PLAYER'


def new_player_connected(number_of_players):
    return json.dumps({
        'type': BE_NEW_PLAYER_CONNECTED,
        'number_of_players': number_of_players
    })


def player_disconnected(number_of_players):
    return json.dumps({
        'type': BE_PLAYER_DISCONNECTED,
        'number_of_players': number_of_players
    })


def game_plus_minus_state(game_counter):
    return json.dumps({
        'type': BE_GAME_PLUS_MINUS_STATE,
        'game_counter': game_counter
    })


def new_thread_was_opened(port):
    return json.dumps({
        'type': BE_NEW_THREAD_WAS_OPENED_TO_YOU,
        'port': port
    })


def waiting_for_second_player():
    return json.dumps({
        'type': BE_WAITING_FOR_SECOND_PLAYER
    })
