import { combineReducers } from "redux";
import { contacts } from "./contacts";
import { numberReducer } from "./numberReducer";

export default combineReducers({
  contacts,
    numeration: numberReducer,
});
