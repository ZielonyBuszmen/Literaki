import asyncio
import json
import websockets



STATE = {'value': 0}

USERS = set()


def state_event():
    return json.dumps({'type': 'state', **STATE})


def users_event():
    return json.dumps({'type': 'users', 'count': len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()




# główna funkcja programu
async def pair_game(websocket, path):
    await websocket.send(json.dumps({'type': 'rozpaczeto gre parowa,'}))
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data['action'] == 'minus':
                STATE['value'] -= 1
                await notify_state()
            elif data['action'] == 'plus':
                STATE['value'] += 1
                await notify_state()
    finally:
        await unregister(websocket)


def start_pair_thread(port=6790):
    print("port dany do nowej gry ", port)
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(pair_game, 'localhost', port))
    asyncio.get_event_loop().run_forever()

