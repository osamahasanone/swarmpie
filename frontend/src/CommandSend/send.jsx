import React, { Component } from "react";
import "antd/dist/antd.css";
import { Row, Col, message, Button } from "antd";
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

  shouldDisableGo = () => {
    const commandVerb = this.state.commandVerb;
    if (commandVerb) {
      return (
        this.state.commandParameters.length !== commandVerb.parameters.length
      );
    }
    return true;
  };

  onGoClick = async () => {
    console.log(this.state.commandVerb);
    console.log(this.state.commandParameters);
    await fetch("http://127.0.0.1:8000/commands/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        verb: this.state.commandVerb.id,
        parameters: this.state.commandParameters,
      }),
    })
      .then((response) => response.json())
      .then((res_json) => message.success(res_json.id));
  };

  render() {
    return (
      <React.Fragment>
        <Row gutter={16}>
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

        <Row className="mt-3" gutter={16}>
          <Col className="gutter-row" span={8}>
            <Button
              style={{ width: "100%" }}
              type="primary"
              onClick={this.onGoClick}
              disabled={this.shouldDisableGo()}
            >
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
