import React from 'react';
import { connect } from 'react-redux';
import Header from './Header.js';
import Quiz from './Quiz.js';
import BottomBar from './BottomBar.js';
import './Game.css';
import { setRedirectToLobby } from "../actions";
import { Col, Row } from "reactstrap";
import Container from "reactstrap/es/Container";

class Game extends React.Component {

  chatMessagesRenderer = (messages) => {
    return messages.map((message) => {
      const date = new Date(message.time * 1000);
      const who = message.isCurrentPlayer ? 'Ja' : 'Przeciwnik';
      const whoClass = message.isCurrentPlayer ? 'player' : 'opponent';

      return <p className='message'>
        <span className={'author ' + whoClass}>{who}</span> &nbsp;
        <span className='hours'>({date.getHours()}:{date.getMinutes()}:{date.getSeconds()})</span> &nbsp;
        {message.message}
      </p>;
    })
  };

  render() {
    if (this.props.redirectToLobby) {
      this.props.setRedirectToLobby(false);
      this.props.history.push('/');
    }

    return (
      <Container fluid>
        <Row><Header category={this.props.category} yourTurn={this.props.yourTurn}/></Row>
        <Row className="GameContent">
          <Col>
            <Quiz catchword={this.props.catchword}/></Col>
          <Col className="chatField" xs="12" sm="3">
            {this.chatMessagesRenderer(this.props.chatMessages)}
          </Col>
        </Row>
        <Row><BottomBar yourTurn={this.props.yourTurn}/></Row>
      </Container>
    );
  }
}

function mapStateToProps(state) {
  return {
    redirectToLobby: state.lobby.redirectToLobby,
    catchword: state.game.catchword,
    category: state.game.category,
    yourTurn: state.game.yourTurn,
    chatMessages: state.chat.messages,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    setRedirectToLobby: (value) => dispatch(setRedirectToLobby(value)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Game);