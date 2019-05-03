export const REDIRECT_TO_GAME = 'REDIRECT_TO_GAME';
export const REDIRECT_TO_LOBBY = 'REDIRECT_TO_LOBBY';
export const FE_SEND_LETTER = 'FE_SEND_LETTER';
export const FE_SEND_CHAT_MESSAGE = 'FE_SEND_CHAT_MESSAGE';

export const BE_NEW_PLAYER_CONNECTED = 'BE_NEW_PLAYER_CONNECTED';
export const BE_NEW_THREAD_WAS_OPENED_TO_YOU = 'BE_NEW_THREAD_WAS_OPENED_TO_YOU';
export const BE_WAITING_FOR_SECOND_PLAYER = 'BE_WAITING_FOR_SECOND_PLAYER';
export const BE_GAME_STATE = 'BE_GAME_STATE';
export const BE_END_OF_YOUR_TURN = 'BE_END_OF_YOUR_TURN';
export const BE_START_OF_YOUR_TURN = 'BE_START_OF_YOUR_TURN';
export const BE_YOU_LOSE_THE_GAME = 'BE_YOU_LOSE_THE_GAME';
export const BE_YOU_WIN_THE_GAME = 'BE_YOU_WIN_THE_GAME';
export const BE_ROUND_NUMBER = 'BE_ROUND_NUMBER';
export const BE_CHAT_MESSAGE = 'BE_CHAT_MESSAGE';
export const BE_PLAYER_DISCONNECTED = 'BE_PLAYER_DISCONNECTED';

export const setRedirectToGame = (value) => ({
  type: REDIRECT_TO_GAME,
  value: value,
});

export const setRedirectToLobby = (value) => ({
  type: REDIRECT_TO_LOBBY,
  value: value,
});

export const sendLetter = (value) => ({
  type: FE_SEND_LETTER,
  value: value,
});

export const sendMessage = (value) => ({
  type: FE_SEND_CHAT_MESSAGE,
  value: value,
});
