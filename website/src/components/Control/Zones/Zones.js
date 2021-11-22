import React, { useState, useEffect } from "react";
import CreateZoneForm from "./CreateZoneForm";



function Zones(){
  const [zones, setZones] = useState([])


  useEffect(() => {
    fetch('/api/get/controlpanel/zones')
    .then(response => response.json())
    .then(data => {
      setZones(data)
    });
  }, []);



  const Zonelist = Object.values(zones).map((zone, index) =>{
    return (
    <tr key={index}>
        <td>{zone.buildingname}</td>
        <td>{zone.zonename}</td>
        <td>{zone.id}</td>
    </tr>
    )
  })

  return (
      <div>
        <p className="ControlPanelTableHeader">Zones</p>
        <table className="ControlPanelTable"> 
            <tbody>
                <tr>
                    <th>Building Name</th>
                    <th>Zone Name</th>
                    <th>ID</th>
                </tr>
                {Zonelist}
            </tbody>
        </table>
        <CreateZoneForm />
      </div>
        
  );

}
export default Zones