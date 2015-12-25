import React from 'react';
import ReactDOM from 'react-dom';
import {Pagination} from 'react-bootstrap';


class Gallery extends React.Component {
  constructor(props){
    super(props);
    this.state = {activePage: 1}
    this.handleSelect = this.handleSelect.bind(this);
  }
  handleSelect(evt, selectedEvent){
    console.log(evt)
    console.log(selectedEvent)
    this.setState({activePage: selectedEvent.eventKey})
  }
  
  render(){
    return (<div>
      <Pagination
        prev
        next
        first
        last
        ellipsis
        items={20}
        maxButtons={5}
        activePage={this.state.activePage}
        onSelect={this.handleSelect} />
    </div>)
  }
}

ReactDOM.render(<Gallery />, document.getElementById('photo-content'));
