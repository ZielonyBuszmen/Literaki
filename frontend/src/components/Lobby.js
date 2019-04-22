import React from 'react';
import {Container, Alert } from 'reactstrap';
import "./Lobby.css";

class Lobby extends React.Component {

    render() {
        return (
            <Container className="Lobby" fluid>
                <Alert color="primary">Prosimy poczekać na dołączenie drugiego gracza.</Alert><br/>
            </Container>
        );
    }
}

export default Lobby;