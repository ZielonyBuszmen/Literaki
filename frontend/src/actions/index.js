export const REDIRECT_TO_GAME = 'REDIRECT_TO_GAME';
export const REDIRECT_TO_LOBBY = 'REDIRECT_TO_LOBBY';
export const FE_SEND_LETTER = 'FE_SEND_LETTER';

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