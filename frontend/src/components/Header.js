import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import "./Header.css";

class Header extends React.Component {

  render() {
    const actualRound = 'ActualRound';
    return (
      <Container className="Header" fluid>
        <Row>
          <Col className={'You ' + actualRound}>
            <b>Ty</b>
          </Col>
          <Col className="Category">
            Nazwa_Kategorii
          </Col>
          <Col className='Opponent '>
            <b>Przeciwnik</b>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Header;