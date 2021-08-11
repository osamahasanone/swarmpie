import React, { Component } from "react";
import CommandParameter from "./commandParameter";

class CommandParameters extends Component {
  render() {
    return (
      <React.Fragment>
        {this.props.parameters.map((parameter) => (
          <CommandParameter
            key={parameter.id}
            parameter={parameter}
            onParameterChoiceChange={this.props.onParameterChoiceChange}
          />
        ))}
      </React.Fragment>
    );
  }
}

export default CommandParameters;
