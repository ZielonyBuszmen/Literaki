import React from 'react';
import { connect } from 'react-redux';
import Header from './Header.js';
import Quiz from './Quiz.js';
import BottomBar from './BottomBar.js';
import './Game.css';

class Game extends React.Component {

  render() {
    return (
      <div>
        <Header/>
        <Quiz/>
        <BottomBar/>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {};
}

function mapDispatchToProps(dispatch) {
  return {};
}

export default connect(mapStateToProps, mapDispatchToProps)(Game);