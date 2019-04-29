import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import "./Quiz.css";

class Quiz extends React.Component {

  render() {
    return (
      <Container className="Quiz" fluid>
        <Row>
          <Col xs="12" sm="9">{this.props.catchword}</Col>
        </Row>
        <Row>
          <Col className="result">{this.props.result}</Col>
        </Row>
      </Container>
    );
  }
}

export default Quiz;
