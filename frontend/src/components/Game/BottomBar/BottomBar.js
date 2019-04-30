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

  sendLetter = (e) => {
    e.preventDefault();
    
    if (this.state.text.length > 0) {
      this.props.websocket.send(JSON.stringify(sendLetter(this.state.text)));
      this.setState({text: ''});
    }
  };


  render() {
    const inputText = this.props.yourTurn ? this.state.text : 'Poczekaj na swoją turę...';
    return (
      <Row className="BottomBar">
        <Col xs="6" md="5" lg="4">
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
        <Col xs="6" md="3" lg="5" className="Round">
          | &nbsp; <b>Runda {this.props.numberRound}</b>
        </Col>
        <Col className="chatInput" xs="12" md="4" lg="3">
          <ChatInput/>
        </Col>
      </Row>
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
