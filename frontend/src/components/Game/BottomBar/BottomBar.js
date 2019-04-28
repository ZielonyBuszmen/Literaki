import React from 'react';
import { Col, Container, Row, InputGroup, Input, InputGroupAddon, Button } from 'reactstrap';
import "./BottomBar.css";
import { connect } from "react-redux";
import { sendLetter } from "../../../actions";
import ChatInput from "./ChatInput";

class BottomBar extends React.Component {

  state = {
    text: '',
  };

  sendLetter = () => {
    if (this.state.text.length > 0) {
      this.props.websocket.send(JSON.stringify(sendLetter(this.state.text)));
      this.setState({text: ''});
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
            <ChatInput/>
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
