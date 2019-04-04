import { createStore } from 'redux';
import reducers from './reducers';

export const initialStoreState = {
    numeration: {
        number: 10,
    }
}

export const store = createStore(reducers, initialStoreState);