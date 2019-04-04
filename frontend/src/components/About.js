import React from 'react';
import {connect} from 'react-redux';
import {setNumber} from '../actions/index'
import './About.css';

class About extends React.Component {

    render() {
        let {number} = this.props.numeration;
        return (
            <div className="container">
                <div className="subtraction" onClick={() => this.props.setNumber(--number)}>
                    <b>-</b>
                </div>
                <div className="number">
                    <b>{number}</b>
                </div>
                <div className="addition" onClick={() => this.props.setNumber(++number)}>
                    <b>+</b>
                </div>
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {
        numeration: state.numeration,
    };
}

function mapDispatchToProps(dispatch) {
    return {
        setNumber: (number) => dispatch(setNumber(number)),
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(About);