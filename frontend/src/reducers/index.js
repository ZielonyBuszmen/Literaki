import {combineReducers} from "redux";
import {lobbyReducer} from "./lobbyReducer";
import {websocketReducer} from "./websocketRedcer";
import {gameReducer} from "./gameReducer";

export default combineReducers({
    lobby: lobbyReducer,
    websocket: websocketReducer,
    game: gameReducer,
});
