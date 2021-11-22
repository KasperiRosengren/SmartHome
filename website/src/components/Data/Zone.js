import React, { useState, useEffect } from 'react'
import OutletBox from './Visuals/Outlets/OutletBox'
//import LineChartTest from './LineChartTest';
import Weather from './Visuals/Weather/Weather';
import Lights from './Visuals/Lights/Lights';

const Zone = props =>{

    const [outletboxes, setOutletBoxes] = useState([props.dataTo.outlets])
    const [weather, setWeather] = useState([{
      temperature: props.dataTo.temperature,
      humidity: props.dataTo.humidity,
      airpressure:  props.dataTo.airpressure,
    }])
    const [lights, setLights] = useState([props.dataTo.lights])

    let outletboxlist = outletboxes.map((outletbox, index)=>{
      if(Object.keys(JSON.parse(outletbox)) !== 0){
        return (
          <div>
            {
              JSON.parse(outletbox).map((box, boxindex)=>{
                //console.log(box.outlets)
                return(
                  <OutletBox info={box.outlets}
                  zone={props.dataTo.Zone}
                  building={props.dataTo.Building}
                  key={boxindex}
                />)
              })}
          </div>
        )
      }
    })

    let weatherlist = weather.map((data, index)=>{
      return(
        <Weather key={index}
          info={data} 
          zone={props.dataTo.Zone}
          building={props.dataTo.Building}
        />)
    })

/*
    let lightlist = lights.map((light, index)=>{
      return(
        <Lights key={index}
          info={data} 
          zone={props.dataTo.Zone}
          building={props.dataTo.Building}
        />)
    })
*/


    let lightlist = lights.map((light, index)=>{
      if(Object.keys(JSON.parse(light)) !== 0){
        return (
          <div className="lights">
            {
              JSON.parse(light).map((data, dataindex)=>{
                //console.log(data.lights)
                return(
                  <Lights info={data}
                  zone={props.dataTo.Zone}
                  building={props.dataTo.Building}
                  key={dataindex}
                />)
              })}
          </div>
        )
      }
    })




    return(
      <div className="zone">
        <div>
        <p className="zoneTitle">{props.dataTo.Building + " / " + props.dataTo.Zone}</p>
        </div>
        <div>
          <p className="zoneTitle">Outlets</p>
          {outletboxlist}
        </div>
        <div>
          <p className="zoneTitle">Weather</p>
          {weatherlist}
        </div>
        <div>
          <p className="zoneTitle">Lights</p>
          <div>{lightlist}</div>
          
        </div>
      </div>
    )


}

export default Zone
