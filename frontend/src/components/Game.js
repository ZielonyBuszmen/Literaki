import React from 'react';
import { connect } from 'react-redux';
import Header from './Header.js';
import Quiz from './Quiz.js';
import BottomBar from './BottomBar.js';
import './Game.css';
import { setRedirectToLobby } from "../actions";

class Game extends React.Component {

  render() {
    if (this.props.redirectToLobby) {
      this.props.setRedirectToLobby(false);
      this.props.history.push('/');
    }
    return (
      <div>
        <Header category={this.props.category} yourTurn={this.props.yourTurn}/>
        <Quiz catchword={this.props.catchword}/>
        <BottomBar yourTurn={this.props.yourTurn}/>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    redirectToLobby: state.lobby.redirectToLobby,
    catchword: state.game.catchword,
    category: state.game.category,
    yourTurn: state.game.yourTurn,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    setRedirectToLobby: (value) => dispatch(setRedirectToLobby(value)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Game);