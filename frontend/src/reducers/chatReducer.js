import {
  BE_CHAT_MESSAGE,
  BE_PLAYER_DISCONNECTED_FROM_GAMEPLAY
} from "../actions";

export const GAME_END = 'GAME_END';

export const chatReducer = (state = [], action) => {
  switch (action.type) {
    case BE_CHAT_MESSAGE:
      return {
        ...state,
        messages: [...state.messages, {
          time: action.time,
          isCurrentPlayer: action.isCurrentPlayer,
          message: action.message
        }],
      };
    case BE_PLAYER_DISCONNECTED_FROM_GAMEPLAY:
      return {
        messages: [...state.messages, {
          message: GAME_END
        }],
      };
    default:
      return state;
  }
};
