import { createStore } from 'redux';
import reducers from './reducers';
import {SERVER, START_PORT} from "./consts";


export const initialStoreState = {
    websocket: {
        websocket: new WebSocket(`ws://${SERVER}:${START_PORT}/`),
    },
    lobby: {
        message: "Łączenie z serwerem...",
        redirectToGame: false,
        redirectToLobby: false,
    }
};

export const store = createStore(reducers, initialStoreState);

initialStoreState.websocket.websocket.onmessage=(event) => {
    const data = JSON.parse(event.data);
    store.dispatch(data);
    console.log(data);
};