import React, { Component } from "react";
import "antd/dist/antd.css";
import { Select, Typography } from "antd";
import ItemDescription from "../common/itemDescription";

const { Option } = Select;
const { Text } = Typography;
class SelectVerb extends Component {
  render() {
    return (
      <div>
        <Text strong className="d-block p-2 bg-primary text-white">
          Verb
        </Text>
        <Select
          showSearch
          size="large"
          className="d-block"
          placeholder="Select a verb"
          optionFilterProp="value"
          onChange={this.props.onChange}
          filterOption={(input, option) =>
            option.props.value.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {this.props.verbs.map((verb) => (
            <Option key={verb.id} value={verb.name}>
              <ItemDescription
                title={verb.name}
                description={verb.description}
              />
            </Option>
          ))}
        </Select>
      </div>
    );
  }
}

export default SelectVerb;
