import React, { useState, useEffect } from 'react';
//import LineChartTest from './LineChartTest';
import Outlet from './Visuals/Outlet';
import Light from './Visuals/Light';
import ChartLine from './Visuals/ChartLine';
import io from 'socket.io-client'
//import { socket } from '../../App';


/*
const TestZoneModular = props =>{
  
    const [outlets, setOutlets] = useState(props.dataTo.outlets)
    const [lights, setLights] = useState(props.dataTo.lights)
    const [name, setName] = useState(props.dataTo.zone)
    const [temperatureD, setTemperatureD] = useState(props.dataTo.temperature.values)
    const [humidity, setHumidity] = useState(props.dataTo.humidity.values)
    const [timestamp, setTimestamp] = useState(props.dataTo.temperature.timestamp)

    
    
    useEffect(() => {
      const socket = io("http://localhost:5000/building/" + name);
      //console.log(socket)
      socket.emit('tester', 'working!')
      //socket.emit('join', {username: 'DisIsName', room: name})
      socket.on("roomData", (data) => {
        //console.log('new data: '+ data.temp)
        setHumidity([...humidity, data.hum])
        setTemperatureD([...temperatureD, data.temp]);
        setTimestamp([...timestamp, data.tst])
        //let { temperature, newData} = temperature
      });
    }, [])
    
    

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
            <div className="graph">
              <h2 className="chartTitle">24H</h2>
              <ChartLine temp={temperatureD} hum={humidity} tst={timestamp} zone={name} />
            </div>
            {lightlist}
        </div>
  );
}
*/


const TestZoneModular = props =>{
  
    const [outlets, setOutlets] = useState(props.dataTo.outlets)
    const [lights, setLights] = useState(props.dataTo.lights)
    const [name, setName] = useState(props.dataTo.zone)
    const [temperatureD, setTemperatureD] = useState(props.dataTo.temperature.values)
    const [humidity, setHumidity] = useState(props.dataTo.humidity.values)
    const [timestamp, setTimestamp] = useState(props.dataTo.temperature.timestamp)

    
    
    useEffect(() => {
      const socket = io("http://localhost:5000/building/" + name);
      //console.log(socket)
      socket.emit('tester', 'working!')
      //socket.emit('join', {username: 'DisIsName', room: name})
      socket.on("roomData", (data) => {
        //console.log('new data: '+ data.temp)
        setHumidity([...humidity, data.hum])
        setTemperatureD([...temperatureD, data.temp]);
        setTimestamp([...timestamp, data.tst])
        //let { temperature, newData} = temperature
      });
    }, [])
    
    

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
            <div className="graph">
              <h2 className="chartTitle">24H</h2>
              <ChartLine temp={temperatureD} hum={humidity} tst={timestamp} zone={name} />
            </div>
            {lightlist}
        </div>
  );
}

export default TestZoneModular
