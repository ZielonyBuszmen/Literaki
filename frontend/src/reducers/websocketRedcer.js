import { SERVER } from "../consts";
import { store } from "../store";


export const websocketReducer = (state = [], action) => {
  switch (action.type) {
    case 'BE_NEW_THREAD_WAS_OPENED_TO_YOU':
      const createWebsocket = new WebSocket(`ws://${SERVER}:${action.port}/`);
      createWebsocket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        store.dispatch(data);
        console.log('gra', data);
      };
      return {...state, websocket: createWebsocket};
    default:
      return state;
  }
};
