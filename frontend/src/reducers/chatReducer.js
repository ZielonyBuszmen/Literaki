import {BE_CHAT_MESSAGE, BE_PLAYER_DISCONNECTED} from "../actions";

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
            case BE_PLAYER_DISCONNECTED:
            return {
                messages: [...state.messages, {
                    time: '',
                    message: 'Twój przeciwnik opuścił grę. Aby zacząć nową grę odśwież stronę.'
                }],
            };
        default:
            return state;
    }
};
