import React, { Component } from 'react';
import {withRouter, Route} from 'react-router-dom'
import Main from './Main';
import About from './About';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Route path="/" exact strict component={Main}/>
        <Route path="/about" component={About}/>
      </div>
    );
  }
}

export default App;
