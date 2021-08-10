import React, { useState, useEffect } from 'react'
import OutletBox from './Visuals/OutletBox'
//import LineChartTest from './LineChartTest';
import io from 'socket.io-client'



const Zone = props =>{

    const [outletboxes, setOutletBoxes] = useState([props.dataTo.outlets.outlets])

    useEffect(() => console.log(outletboxes), [outletboxes]);

    let outletboxlist = outletboxes.map((outletbox, index)=>{
        return <OutletBox info={outletboxes[index]}
                    zone={props.dataTo.Zone}
                    building={props.dataTo.Building}
                    key={index}
                />
      })
    return(
        <div>
            <p>Här är zone name</p>
            {outletboxlist}
            <p>Some lightes för zöne</p>
        </div>
        
    )


    /*
    useEffect(() => {
      const socket = io("http://localhost:5000/building/" + name);
      socket.emit('tester', 'working!')
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

  return (
    <div className="zone">
            <div className="zoneTitle">{name}</div>
            <div className="outlets">
                {outletlist}
            </div>
        </div>
  );
  */
}

export default Zone
