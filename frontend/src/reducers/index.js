import {combineReducers} from "redux";
import {lobbyReducer} from "./lobbyReducer";

export default combineReducers({
    lobby: lobbyReducer
});
