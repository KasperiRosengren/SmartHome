import React, { useState, useEffect } from "react";
//import RealZone from './Visualization/RealZone';
import TestZoneModular from './Visualization/TestZoneModular'
import io from 'socket.io-client'
/*
function Devices(){
  const [zones, setZones] = useState([])
  useEffect(() => {
    fetch('/api/test/test')
    .then(response => response.json())
    .then(data => setZones(data))
  }, []);

  let listzone = Object.keys(zones).map((zone, index)=>{
    console.log(zones[index])
    return <TestZoneModular dataTo={zones[index]} key={index} />
  })

    return (
        <div className="LayoutTestMain">
            {listzone}
        </div>
      );
}
*/
function Devices(){
  const [zones, setZones] = useState([])
  useEffect(() => {
    fetch('/api/test/test')
    .then(response => response.json())
    .then(data => setZones(data))
  }, []);

  let listzone = Object.keys(zones).map((zone, index)=>{
    console.log(zones[index])
    return <TestZoneModular dataTo={zones[index]} key={index} />
  })

    return (
        <div className="LayoutTestMain">
            {listzone}
        </div>
      );
}
export default Devices