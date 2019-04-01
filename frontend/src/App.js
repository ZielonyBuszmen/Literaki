import React, { Component } from 'react';
import {withRouter, Route} from 'react-router-dom'
import Main from './components/Main';
import About from './components/About';
import { connect } from "react-redux";
import { contactsFetched } from "./actions";

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

const mapStateToProps = (state) => {
  return {
    contacts: state.contacts
  }
};

const mapDispatchToProps = {contactsFetched};

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(App));
