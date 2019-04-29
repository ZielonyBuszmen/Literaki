import React from 'react';
import { connect } from 'react-redux';
import './Game.css';
import Container from "reactstrap/es/Container";

class ChatField extends React.Component {

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
    return (
      <Container fluid>
        {this.chatMessagesRenderer(this.props.chatMessages)}
      </Container>
    );
  }
}

function mapStateToProps(state) {
  return {
    chatMessages: state.chat.messages,
  };
}

function mapDispatchToProps() {
  return {};
}

export default connect(mapStateToProps, mapDispatchToProps)(ChatField);