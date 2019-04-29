import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import "./Header.css";

class Header extends React.Component {
  render() {
    const youStyle = this.props.yourTurn ? 'ActualRound' : '';
    const opponentStyle = !this.props.yourTurn ? 'ActualRound' : '';
    return (
      <Row className="Header">
        <Col md="4" sm="6">
          <span className="Players">
            <b className={'player-label ' + youStyle}>TY</b>
            :
            <b className={'player-label  ' + opponentStyle}>RYWAL</b>
          </span>
        </Col>
        <Col md="4" sm="6" className="Category">
          {this.props.category}
        </Col>
        <Col md='4' className='d-none d-sm-block'>
        </Col>
      </Row>
    );
  }
}

export default Header;
