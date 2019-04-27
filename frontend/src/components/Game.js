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
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>
            dad <br/>d
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
  };
}

function mapDispatchToProps(dispatch) {
  return {
    setRedirectToLobby: (value) => dispatch(setRedirectToLobby(value)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Game);