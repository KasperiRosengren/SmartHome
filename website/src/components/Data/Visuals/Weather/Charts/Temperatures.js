import React, { useState, useEffect} from 'react';
import DailyChart from './DailyChart';


const Temperatures = props =>{
            
    const [zone, setZone] = useState(props.match.params.zoneName)
    const [building, setBuilding] = useState(props.match.params.buildingName)
    const [temperatures, setTemperatures] = useState({})
    useEffect(() => {
        fetch('/api/get/zone/temperature/daily',{
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    building:building,
                    zone: zone})})
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    setTemperatures(data)
                    })
    }, [])


    const tempChartList = Object.entries(temperatures).map((temperature, index)=>{
        console.log(temperature[1].name)
        console.log(temperature[1].lastday)
        console.log(JSON.parse(temperature[1].lastday).time)
        console.log(JSON.parse(temperature[1].lastday).temperature)
        return (<DailyChart data={{
            time: JSON.parse(temperature[1].lastday).time,
            values: JSON.parse(temperature[1].lastday).temperature
            }}
            deviceName={temperature[1].name}
            dataType="Temperature"
            zone={zone}
            building={building}
            key={index} />)
      })

   return(
       <div style={{
        margin: "5%",
        boxShadow: "0 0 5px 2px rgba(0, 0, 0, .3)",
        borderRadius: "5%"
       }}>
           <h2 className="chartTitle">Daily</h2>
           {tempChartList}
       </div>
   )
}

export default Temperatures
