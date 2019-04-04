export const SET_NUMBER = 'SET_NUMBER';

export const numberReducer = (state = [], action) => {
    switch (action.type) {
        case SET_NUMBER:
            return {...state, number: action.number};
        default:
            return state;
    }
};