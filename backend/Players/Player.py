class Player:
    def __init__(self, websocket, name):
        self.websocket = websocket
        self.name = name

    def get_websocket(self):
        return self.websocket

    def get_name(self):
        return self.name

