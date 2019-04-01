import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Main extends Component {
  render() {
    return (
      <div>
        LITERAKI TO FAJNA GIERA
          <Link to="/About">
              About
            </Link>
      </div>
    );
  }
}

export default Main;