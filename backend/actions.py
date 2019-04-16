# Lista message, które będą przesyłane przez websocket
# message zaczynające się na BE_ pochodzą z serwera (backendu)
# message zaczynające się na FE_ pochodzą od klienta (frontendu)

import json

BE_NEW_PLAYER_CONNECTED = 'BE_NEW_PLAYER_CONNECTED'
BE_PLAYER_DISCONNECTED = 'BE_PLAYER_DISCONNECTED'
BE_NEW_THREAD_WAS_OPENED_TO_YOU = 'BE_NEW_THREAD_WAS_OPENED_TO_YOU'
BE_WAITING_FOR_SECOND_PLAYER = 'BE_WAITING_FOR_SECOND_PLAYER'
BE_GAME_WAS_STARTED = 'BE_GAME_WAS_STARTED'
BE_GAME_STATE = 'BE_GAME_STATE'
BE_END_OF_YOUR_TURN = 'BE_END_OF_YOUR_TURN'
BE_START_OF_YOUR_TURN = 'BE_START_OF_YOUR_TURN'
BE_YOU_LOSE_THE_GAME = 'BE_YOU_LOSE_THE_GAME'
BE_YOU_WIN_THE_GAME = 'BE_YOU_WIN_THE_GAME'
BE_NOT_YOUR_TURN = 'BE_NOT_YOUR_TURN'
BE_UNSUPPORTED_ACTION = 'BE_UNSUPPORTED_ACTION'

FE_SEND_LETTER = 'FE_SEND_LETTER'


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


def new_thread_was_opened(port):
    return json.dumps({
        'type': BE_NEW_THREAD_WAS_OPENED_TO_YOU,
        'port': port
    })


def waiting_for_second_player():
    return json.dumps({
        'type': BE_WAITING_FOR_SECOND_PLAYER
    })


def game_was_started():
    return json.dumps({
        'type': BE_GAME_WAS_STARTED
    })


def send_game_state(state):
    return json.dumps({
        'type': BE_GAME_STATE,
        **state
    })


def player_end_turn():
    return json.dumps({
        'type': BE_END_OF_YOUR_TURN
    })


def player_start_turn():
    return json.dumps({
        'type': BE_START_OF_YOUR_TURN
    })


def player_lose_game():
    return json.dumps({
        'type': BE_YOU_LOSE_THE_GAME
    })


def player_win_game():
    return json.dumps({
        'type': BE_YOU_WIN_THE_GAME
    })


def not_your_turn():
    return json.dumps({
        'type': BE_NOT_YOUR_TURN
    })


def unsupported_action():
    return json.dumps({
        'type': BE_UNSUPPORTED_ACTION
    })
