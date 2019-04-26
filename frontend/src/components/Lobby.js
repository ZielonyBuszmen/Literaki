import React from 'react';
import { Container, Alert } from 'reactstrap';
import "./Lobby.css";
import { connect } from "react-redux";
import { setRedirectToGame } from "../actions";

class Lobby extends React.Component {

  render() {
    const info = this.props.message;
    if (this.props.redirectToGame) {
      this.props.setRedirectToGame(false);
      this.props.history.push('/game');
    }
    return (
      <Container className="Lobby" fluid>
        <Alert color="primary">{info}</Alert>
      </Container>
    );
  }
}

function mapStateToProps(state) {
  return {
    message: state.lobby.message,
    redirectToGame: state.lobby.redirectToGame,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    setRedirectToGame: (value) => dispatch(setRedirectToGame(value)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Lobby);