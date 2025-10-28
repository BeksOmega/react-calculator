import React from "react";
import PropTypes from "prop-types";
import { Textfit } from "react-textfit";

import "./Display.css";

export default class Display extends React.Component {
  static propTypes = {
    value: PropTypes.string,
  };

  render() {
    return (
      <div className="component-display">
        <Textfit mode="single" max={70}>
          {this.props.value}
        </Textfit>
      </div>
    );
  }
}
