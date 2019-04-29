export const lobbyReducer = (state = [], action) => {
  switch (action.type) {
    case 'BE_NEW_PLAYER_CONNECTED':
      if (action.number_of_players === 2)
        return {...state, message: "Trwa łączenie z drugim graczem..."};
      return state;
    case 'BE_WAITING_FOR_SECOND_PLAYER':
      return {
        ...state,
        message: "Oczekiwanie na drugiego gracza...",
        redirectToGame: false,
        redirectToLobby: true,
      };
    case 'BE_NEW_THREAD_WAS_OPENED_TO_YOU':
      return {
        ...state,
        redirectToGame: true,
        redirectToLobby: false,
      };
    default:
      return state;
  }
};
