import {
  BE_END_OF_YOUR_TURN,
  BE_GAME_STATE, BE_ROUND_NUMBER,
  BE_START_OF_YOUR_TURN,
  BE_YOU_LOSE_THE_GAME,
  BE_YOU_WIN_THE_GAME
} from "../actions";

export const gameReducer = (state = [], action) => {
  switch (action.type) {
    case BE_GAME_STATE:
      return {
        ...state,
        catchword: action.catchword,
        category: action.category,
      };
    case BE_START_OF_YOUR_TURN:
      return {
        ...state,
        yourTurn: true,
      };
    case BE_END_OF_YOUR_TURN:
      return {
        ...state,
        yourTurn: false,
      };
    case BE_ROUND_NUMBER:
      return {
        ...state,
        numberRound: action.value,
      };
    case BE_YOU_LOSE_THE_GAME:
      return {
        ...state,
        result: 'PRZEGRAŁEŚ :(',
      };
    case BE_YOU_WIN_THE_GAME:
      return {
        ...state,
        result: 'WYGRAŁEŚ!!!!',
      };
    default:
      return state;
  }
};
