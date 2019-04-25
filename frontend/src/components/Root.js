import React from 'react';
import { HashRouter as Router } from 'react-router-dom'
import App from '../App';

const Root = () =>
    <Router basename={process.env.PUBLIC_URL}>
      <App/>
    </Router>

export default Root;