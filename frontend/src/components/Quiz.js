import React from 'react';
import { Container } from 'reactstrap';
import "./Quiz.css";

class Quiz extends React.Component {

  render() {
    return (
      <Container className="Quiz">
        {this.props.catchword}
        {/*_ _ _ _ _ &nbsp; _ _ _ _ _ &nbsp; _ _ _ _ _*/}
      </Container>
    );
  }
}

export default Quiz;