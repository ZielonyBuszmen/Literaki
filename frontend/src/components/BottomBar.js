import React from 'react';
import { Col, Container, Row, InputGroup, Input, InputGroupAddon, Button } from 'reactstrap';
import "./BottomBar.css";
import { connect } from "react-redux";
import { sendLetter, sendMessage } from "../actions";

class BottomBar extends React.Component {

  state = {
    text: '',
    message: '',
  };

  sendLetter = () => {
    if (this.state.text.length > 0) {
      this.props.websocket.send(JSON.stringify(sendLetter(this.state.text)));
      this.setState({text: ''});
    }
  };

  sendMessage = (e) => {
    e.preventDefault();
    if (this.state.message.length > 0) {
      this.props.websocket.send(JSON.stringify(sendMessage(this.state.message)));
      this.setState({message: ''});
    }
  };


  render() {
    const inputText = this.props.yourTurn ? this.state.text : 'Poczekaj na swoją turę...';
    return (
      <Container className="BottomBar" fluid>
        <Row>
          <Col xs="4" sm="4">
            <form>
              <InputGroup>
                <Input disabled={!this.props.yourTurn} value={inputText} onChange={(e) => {
                  this.setState({text: e.target.value})
                }}/>
                <InputGroupAddon addonType="append">
                  <Button type="submit" disabled={!this.props.yourTurn} color="success"
                          onClick={this.sendLetter}>Wyślij</Button>
                </InputGroupAddon>
              </InputGroup>
            </form>
          </Col>
          <Col xs="5" sm="5" className="Round">
            | &nbsp; <b>Runda {this.props.numberRound}</b>
          </Col>
          <Col className="chatInput" xs="3" sm="3">
            <form>
              <InputGroup>
                <Input value={this.state.message} onChange={e => this.setState({message: e.target.value})}
                       placeholder="Wpisz wiadomość"/>
                <InputGroupAddon addonType="append">
                  <Button type="submit" onClick={this.sendMessage} color="info">-></Button>
                </InputGroupAddon>
              </InputGroup>
            </form>
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
