import React, { Component } from 'react';
import {withRouter, Route} from 'react-router-dom'
import Game from './components/Game.js';
import Lobby from './components/Lobby.js';
import { connect } from "react-redux";
import { contactsFetched } from "./actions";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Route path="/" exact strict component={Game}/>
        <Route path="/lobby" component={Lobby}/>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    contacts: state.contacts
  }
};

const mapDispatchToProps = {contactsFetched};

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(App));
