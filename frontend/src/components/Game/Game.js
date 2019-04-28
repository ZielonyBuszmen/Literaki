import React from 'react';
import { connect } from 'react-redux';
import Header from './Header/Header.js';
import Quiz from './Quiz/Quiz.js';
import BottomBar from './BottomBar/BottomBar.js';
import './Game.css';
import { setRedirectToLobby } from "../../actions";
import { Col, Row } from "reactstrap";
import Container from "reactstrap/es/Container";
import ChatField from './ChatField.js';

class Game extends React.Component {

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
            <Quiz result={this.props.result} catchword={this.props.catchword}/></Col>
          <Col className="chatField" xs="12" sm="3">
            <ChatField/>
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
    result: state.game.result,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    setRedirectToLobby: (value) => dispatch(setRedirectToLobby(value)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Game);