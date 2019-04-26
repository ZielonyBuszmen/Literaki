import React, { Component } from 'react';
import { withRouter, Route } from 'react-router-dom'
import Game from './components/Game.js';
import Lobby from './components/Lobby.js';
import { connect } from "react-redux";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Route path="/" exact strict component={Lobby}/>
        <Route path="/game" component={Game}/>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    contacts: state.contacts
  }
};

const mapDispatchToProps = {};

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(App));
