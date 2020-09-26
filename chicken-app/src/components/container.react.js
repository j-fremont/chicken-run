import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import MyCard from './card.react'

export default class MyContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: null
    };
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
        60000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    fetch('http://192.168.1.62:5000/get_image', {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': 0
      }
    })
    .then((response) => response.blob())
    .then((blob) => {
      let newurl = URL.createObjectURL(blob);
      this.setState({
        url: newurl
      });

    });
  }

  render() {
    return (
      <Container fluid={true}>
        <Row>
          <Col xs="8">
            <MyCard url={this.state.url}/>
          </Col>
        </Row>
      </Container>
    );
  }
}
