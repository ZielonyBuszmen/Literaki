import React from 'react';
import {Row, Col} from 'reactstrap';
import "./Quiz.css";

class Quiz extends React.Component {
        render() {
        let infoTurn = this.props.yourTurn ? 'Twoja tura!' : '';
        if(this.props.result!== "") infoTurn = '';
        return (
            <div className="Quiz h-100">
                <Row className='align-items-center h-75'>
                    <Col className='catchword col-xl-6 col-lg-10 col-sm-12 mx-auto'>{this.props.catchword}</Col>
                </Row>
                <Row>
                    <Col className="result">{this.props.result}</Col>
                </Row>
                <Row>
                    <Col id="blok" className="infoTurn">{infoTurn}</Col>
                </Row>
            </div>
        );
    }
}

export default Quiz;
