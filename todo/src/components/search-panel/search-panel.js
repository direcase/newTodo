import React, {Component} from 'react';

import './search-panel.css';
 export default class SearchPanel extends Component{

  state={
    text: ''
  }
  onMySearch=(t)=>{
    const text=t.target.value;
    this.setState({text});
    this.props.onMySearch(text);
  }
  render(){
    return (
      <input type="text"
                className="form-control search-input"
                onChange={this.onMySearch}
                placeholder="type to search"
                value={this.state.text} />
    );
  }
 }

