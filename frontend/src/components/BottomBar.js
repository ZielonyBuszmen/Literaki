import React from 'react';
import { Col, Container, Row, InputGroup, Input, InputGroupAddon, Button } from 'reactstrap';
import "./BottomBar.css";
import { connect } from "react-redux";
import { sendLetter } from "../actions";

class BottomBar extends React.Component {

  state = {
    text: '',
  };

  sendLetter = () => {
    console.log(this.state.text);
    if (this.state.text.length > 0) {
      this.props.websocket.send(JSON.stringify(sendLetter(this.state.text)))
    }
  };


  render() {
    return (
      <Container className="BottomBar" fluid>
        <Row>
          <Col xs="4" sm="4">
            <InputGroup>
              <Input disabled={!this.props.yourTurn} value={this.state.text} onChange={(e) => {
                this.setState({text: e.target.value})
              }}/>
              <InputGroupAddon addonType="append">
                <Button color="success" onClick={this.sendLetter}>Wyślij</Button>
              </InputGroupAddon>
            </InputGroup>
          </Col>
          <Col xs="8" sm="8" className="Round">
            <b>Runda {this.props.numberRound}</b>
          </Col>
        </Row>
      </Container>
    );
  }
}

function mapStateToProps(state) {
  return {
    websocket: state.websocket.websocket,
    numberRound: state.game.numberRound,
  };
}

function mapDispatchToProps(dispatch) {
  return {};
}

export default connect(mapStateToProps, mapDispatchToProps)(BottomBar);
