import React, { Component } from "react";
import "./commandSend.css";
import "antd/dist/antd.css";
import { Row, Col, Button } from "antd";
import { ThunderboltOutlined } from "@ant-design/icons";
import SelectVerb from "./selectVerb";
import CommandParameters from "./commandParameters";

class CommandSend extends Component {
  state = {
    verbs: [],
    commandVerb: null,
    commandParameters: [],
  };

  constructor() {
    super();
    this.onVerbChange = this.onVerbChange.bind(this);
    this.onParameterChoiceChange = this.onParameterChoiceChange.bind(this);
  }
  async componentDidMount() {
    const verbs = await this.fetchVerbs();
    this.setState({ verbs });
  }

  fetchVerbs = async () => {
    const response = await fetch("http://127.0.0.1:8000/common/verbs");
    const verbs = await response.json();
    return verbs;
  };

  onVerbChange(value) {
    const verbs = this.state.verbs.filter((verb) => verb.name === value);
    this.setState({ commandVerb: verbs[0], commandParameters: [] });
  }

  onParameterChoiceChange = (verbParameterID, value) => {
    const commandParameters = [...this.state.commandParameters];
    let param = commandParameters.find((p) => {
      return p.verb_parameter === verbParameterID;
    });
    if (param === undefined)
      commandParameters.push({ verb_parameter: verbParameterID, value: value });
    else param.value = value;

    this.setState({ commandParameters });
  };

  render() {
    console.log(this.state.commandVerb);
    console.log(this.state.commandParameters);
    return (
      <React.Fragment>
        <Row className="group" gutter={16}>
          <Col className="gutter-row" span={8}>
            <SelectVerb verbs={this.state.verbs} onChange={this.onVerbChange} />
          </Col>
        </Row>

        {this.state.commandVerb && (
          <CommandParameters
            parameters={this.state.commandVerb.parameters}
            onParameterChoiceChange={this.onParameterChoiceChange}
          />
        )}

        <Row className="group" gutter={16}>
          <Col className="gutter-row" span={8}>
            <Button type="primary" style={{ width: 300 }}>
              GO
              <ThunderboltOutlined />
            </Button>
          </Col>
        </Row>
      </React.Fragment>
    );
  }
}

export default CommandSend;
