import React, { Component } from "react";
import "antd/dist/antd.css";
import { Typography, Space } from "antd";

const { Text } = Typography;

class ItemDescription extends Component {
  render() {
    return (
      <React.Fragment>
        <Space direction="vertical">
          <Text strong>{this.props.title}</Text>
          <Text type="secondary">{this.props.description}</Text>
        </Space>
      </React.Fragment>
    );
  }
}

export default ItemDescription;
