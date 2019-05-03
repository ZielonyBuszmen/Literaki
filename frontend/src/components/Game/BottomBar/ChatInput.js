import React from 'react';
import { InputGroup, Input, InputGroupAddon, Button } from 'reactstrap';
import { connect } from "react-redux";
import { sendMessage } from "../../../actions";

class ChatInput extends React.Component {

  state = {
    message: '',
  };

  sendMessage = (e) => {
    e.preventDefault();
    if (this.state.message.length > 0) {
      this.props.websocket.send(JSON.stringify(sendMessage(this.state.message)));
      this.setState({message: ''});
    }
  };

  render() {
    return (
      <div className="ChatInput">
        <form>
          <InputGroup>
            <Input value={this.state.message}
                   onChange={e => this.setState({message: e.target.value})}
                   placeholder="Wpisz wiadomość"
            />
            <InputGroupAddon addonType="append">
              <Button type="submit" onClick={this.sendMessage} color="info">-></Button>
            </InputGroupAddon>
          </InputGroup>
        </form>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    websocket: state.websocket.websocket,
  };
}

function mapDispatchToProps(dispatch) {
  return {};
}

export default connect(mapStateToProps, mapDispatchToProps)(ChatInput);
