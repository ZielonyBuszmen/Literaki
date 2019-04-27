export const chatReducer = (state = [], action) => {
  switch (action.type) {
    case 'BE_CHAT_MESSAGE':
      return {
        ...state,
        messages: [...state.messages, {
          time: action.time,
          isCurrentPlayer: action.isCurrentPlayer,
          message: action.message
        }],
      };
    default:
      return state;
  }
};
