import React from 'react';
import ReactDOM from 'react-dom';
import { store } from "./store";
import { Provider } from "react-redux";
import Root from './components/Root';

ReactDOM.render(
  <Provider store={store}>
    <Root/>
  </Provider>,
  document.getElementById('root')
);
