import {combineReducers} from "redux";
import {lobbyReducer} from "./lobbyReducer";
import {websocketReducer} from "./websocketRedcer";

export default combineReducers({
    lobby: lobbyReducer,
    websocket: websocketReducer,
});
