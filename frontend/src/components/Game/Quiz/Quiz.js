import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import "./Quiz.css";

class Quiz extends React.Component {

  render() {
    return (
      <div className="Quiz h-100">
        <Row className='align-items-center h-75'>
          <Col className='catchword col-xl-6 col-lg-10 col-sm-12 mx-auto'>{this.props.catchword}</Col>
        </Row>
        <Row>
          <Col className="result">{this.props.result}</Col>
        </Row>
      </div>
    );
  }
}

export default Quiz;
