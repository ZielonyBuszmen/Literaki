import React from 'react';
import {Container, Row, Col} from 'reactstrap';
import "./Header.css";

class Header extends React.Component {

    render() {

        const youStyle = this.props.yourTurn ? 'ActualRound' : '';
        const opponentStyle = !this.props.yourTurn ? 'ActualRound' : '';
        return (
            <Container className="Header" fluid>
                <Row>
                    <Col className={'You ' + youStyle}>
                        <b>Ty</b>
                    </Col>
                    <Col className="Category">
                        {this.props.category}
                    </Col>
                    <Col className={'Opponent ' + opponentStyle}>
                        <b>Przeciwnik</b>
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Header;