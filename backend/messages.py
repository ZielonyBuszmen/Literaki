# Lista message, które będą przesyłane przez websocket

import json


def new_player_connected(number_of_players):
    return json.dumps({'type': 'NEW_PLAYER_CONNECTED', 'number_of_players': number_of_players})


def player_disconnected(number_of_players):
    return json.dumps({'type': 'PLAYER_DISCONNECTED', 'number_of_players': number_of_players})


def game_plus_minus_state(game_counter):
    return json.dumps({'type': 'GAME_PLUS_MINUS_STATE', 'game_counter': game_counter})
