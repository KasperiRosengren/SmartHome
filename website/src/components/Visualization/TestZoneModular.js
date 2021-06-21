import React, { useState, useEffect } from 'react';
import LineChartTest from './LineChartTest';
import Outlet from './Outlet';
import Light from './Light';

/*
export default class TestZoneModular extends React.Component {
    render() {
        let outletlist = this.props.dataTo.outlets.map((outlet, index)=>{
            return <Outlet info={outlet} key={index}/>
          })
        let lightlist = this.props.dataTo.lights.map((light, index)=>{
            return <Light info={light} key={index}/>
        })
      return (
        <div className="zone">
                <div className="zoneTitle">{this.props.dataTo.zone}</div>
                <div className="outlets">
                    {outletlist}
                </div>
                <div className="graph"><LineChartTest /></div>
                {lightlist}
            </div>
      );
    }
  }
*/


const TestZoneModular = props =>{
    const [outlets, setOutlets] = useState(props.dataTo.outlets)
    const [lights, setLights] = useState(props.dataTo.lights)
    const [name, setName] = useState(props.dataTo.zone)

    let outletlist = outlets.map((outlet, index)=>{
        return <Outlet info={outlets[index]} zone={name} key={index}/>
      })
    let lightlist = lights.map((light, index)=>{
        return <Light info={lights[index]} zone={name} key={index}/>
    })
  return (
    <div className="zone">
            <div className="zoneTitle">{name}</div>
            <div className="outlets">
                {outletlist}
            </div>
            <div className="graph"><LineChartTest /></div>
            {lightlist}
        </div>
  );
}
export default TestZoneModular
