import {
    SET_NUMBER,
} from '../reducers/numberReducer';

export const contactsFetched = (contacts) => ({
    type: 'FETCH_CONTACTS_SUCCESS',
    contacts
});

export function setNumber(number) {
    return {
        type: SET_NUMBER,
        number: number,
    };
}
