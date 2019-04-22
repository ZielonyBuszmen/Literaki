import React from 'react';
import { Col, Container, Row, InputGroup, Input, InputGroupAddon, Button } from 'reactstrap';
import "./BottomBar.css";

class BottomBar extends React.Component {

  render() {
    return (
      <Container className="BottomBar" fluid>
        <Row>
          <Col xs="4" sm="4">
            <InputGroup>
              <Input/>
              <InputGroupAddon addonType="append">
                <Button color="success">Wyślij</Button>
              </InputGroupAddon>
            </InputGroup>
          </Col>
          <Col xs="8" sm="8" className="Round">
            <b>Runda Nr_Rundy</b>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default BottomBar;