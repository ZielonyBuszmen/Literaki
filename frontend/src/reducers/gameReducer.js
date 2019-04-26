export const gameReducer = (state = [], action) => {
    switch (action.type) {
        case 'BE_GAME_STATE':
            return {
                ...state,
                catchword: action.catchword,
                category: action.category,
            };
        case 'BE_START_OF_YOUR_TURN':
            return {
                ...state,
                yourTurn: true,
            };
        case 'BE_END_OF_YOUR_TURN':
            return {
                ...state,
                yourTurn: false,
            };
           case 'BE_ROUND_NUMBER':
              return {
                ...state,
                numberRound: action.value,
            };
        default:
            return state;
    }
}