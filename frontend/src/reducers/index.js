import { combineReducers } from "redux";
import { lobbyReducer } from "./lobbyReducer";
import { websocketReducer } from "./websocketRedcer";
import { gameReducer } from "./gameReducer";
import { chatReducer } from "./chatReducer";

export default combineReducers({
  lobby: lobbyReducer,
  websocket: websocketReducer,
  game: gameReducer,
  chat: chatReducer,
});
