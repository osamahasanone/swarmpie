import React, { Component } from "react";
import "./commandSend.css";
import "antd/dist/antd.css";
import { Row, Col, Select, Input, InputNumber, Typography } from "antd";
import ItemDescription from "../common/itemDescription";

const { Option } = Select;
const { Text } = Typography;

class SelectParameterChoice extends Component {
  getTitle = (choice) => {
    return choice.header === ""
      ? choice.value
      : `${choice.header}=${choice.value}`;
  };

  render() {
    return (
      <Select
        showSearch
        size="large"
        className="Parameter-Input"
        placeholder="Select a Choice"
        optionFilterProp="value"
        onChange={this.props.onChange}
        filterOption={(input, option) =>
          option.props.value.toLowerCase().indexOf(input.toLowerCase()) >= 0
        }
      >
        {this.props.choices.map((choice) => (
          <Option key={choice.id} value={this.getTitle(choice)}>
            <ItemDescription
              title={this.getTitle(choice)}
              description={choice.description}
            />
          </Option>
        ))}
      </Select>
    );
  }
}

class CommandParameter extends Component {
  state = {
    free_value_type: null,
    current_header: "",
  };

  onParameterChoiceChange = (value) => {
    const free_value_types = ["rate", "seconds", "free_text", "msg_id"];
    let is_free = false;
    for (const free_value_type of free_value_types) {
      if (value.includes(free_value_type)) {
        this.setState({ free_value_type });
        is_free = true;
        if (value.includes("=")) {
          const header = value.split("=")[0];
          this.setState({ current_header: `${header}` });
        }
      }
    }
    if (!is_free) {
      this.setState({ free_value_type: null });
      this.props.onParameterChoiceChange(this.props.parameter.id, value);
    }
  };

  onFreeInputChange = (value) => {
    const value_to_send = this.state.current_header
      ? `${this.state.current_header}=${value}`
      : value;
    this.props.onParameterChoiceChange(this.props.parameter.id, value_to_send);
  };

  renderFreeInput = () => {
    if (this.state.free_value_type === "rate")
      return (
        <InputNumber
          className="Parameter-Input"
          onChange={this.onFreeInputChange}
          placeholder="Please enter the rate"
          size="large"
          min={1}
          max={100000}
        />
      );
    else if (this.state.free_value_type === "seconds")
      return (
        <InputNumber
          className="Parameter-Input"
          onChange={this.onFreeInputChange}
          placeholder="Please enter the seconds"
          size="large"
          min={1}
          max={100000}
        />
      );
    else if (this.state.free_value_type === "msg_id")
      return (
        <InputNumber
          className="Parameter-Input"
          onChange={this.onFreeInputChange}
          placeholder="Please enter Message ID"
          size="large"
          min={1}
          max={100000}
        />
      );
    else if (this.state.free_value_type === "free_text")
      return (
        <Input
          className="Parameter-Input"
          onChange={this.onFreeInputChange}
          placeholder="Please enter the Data"
          size="large"
        />
      );
  };

  render() {
    return (
      <div className="parameter">
        <Row gutter={16}>
          <Col className="gutter-row" span={6}>
            <Text strong className="Text">
              Parameter {this.props.parameter.order}
            </Text>
            <SelectParameterChoice
              choices={this.props.parameter.choices}
              onChange={this.onParameterChoiceChange}
            />
          </Col>
        </Row>
        {this.state.free_value_type && (
          <Row gutter={16}>
            <Col className="gutter-row" span={6}>
              {this.renderFreeInput()}
            </Col>
          </Row>
        )}
      </div>
    );
  }
}

export default CommandParameter;
