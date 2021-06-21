import React from 'react';
import OneZone from './Visualization/OneZone';

let zones=['z','z','z','z','z','z','z','z','z'];
let zonelist=zones.map((zone,index)=>{
    return <OneZone key={index} />
  })

export default class LayoutTest extends React.Component {
    render() {
      return (
        <div className="LayoutTestMain">
            {zonelist}
        </div>
      );
    }
  }
  