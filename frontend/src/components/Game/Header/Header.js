import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import "./Header.css";

class Header extends React.Component {
  render() {
    const youStyle = this.props.yourTurn ? 'ActualRound' : '';
    const opponentStyle = !this.props.yourTurn ? 'ActualRound' : '';
    return (
      <Container className="Header" fluid>
        <Row>
          <Col>
            <div className="Players">
            <b className={'player-label ' + youStyle}>TY</b> :
            <b className={'player-label  ' + opponentStyle}>RYWAL</b>
            </div>
          </Col>
          <Col className="Category">
            {this.props.category}
          </Col>
          <Col>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Header;
