import React from 'react';
import { connect } from 'react-redux';
import './Game.css';
import { GAME_END } from "../../reducers/chatReducer";

class ChatField extends React.Component {

  endGameMessageRenderer = () =>
    <p className='message'>
      <span className='noActive'>
        Twój przeciwnik opuścił grę. Aby rozpocząć nową grę, odśwież stronę lub kliknij w poniższy przycisk.
      </span>
      <div className='text-center'>
        <a className='mt-3 btn btn-success' href='/'>
          Nowa Gra
        </a>
      </div>
    </p>;

  chatMessagesRenderer = (messages) => {
    return messages.map((message) => {
      if (message.message === GAME_END) {
        return this.endGameMessageRenderer();
      }

      const date = new Date(message.time * 1000);
      const who = message.isCurrentPlayer ? 'Ja' : 'Rywal';
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
      <div className="mt-3">
        {this.chatMessagesRenderer(this.props.chatMessages)}
      </div>
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