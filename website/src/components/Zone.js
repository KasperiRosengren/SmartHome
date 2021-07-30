import React, { useState, useEffect } from "react";
import ZoneTestThing from './Visualization/ZoneTestThing'
import io from 'socket.io-client'

function Data(){
  const [zones, setZones] = useState(this.props.zones)
  //Sets buildings like = buildName: NiceBuilding, addr: MyStreet 30, Zones: [zone1, zone2, zone3]
  //All buyilding are objects in a array
  useEffect(() => {
    fetch('/api/get/user/buildings')
    .then(response => response.json())
    .then(data => setBuildings(data))
  }, []);

  //Create list of all buildings and pass zones

  let listzone = Object.keys(zones).map((zone, index)=>{
    console.log(zones[index])
    return <ZoneTestThing
            dataTo={zones[index]}
            key={index}
            />
  })

    return (
        <div className="LayoutTestMain">
            {listzone}
        </div>
      );
}
export default Data