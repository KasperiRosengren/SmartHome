import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';



function ControlBuildings(){
  const [buildings, setBuildings] = useState([])


  useEffect(() => {
    fetch('/api/get/controlpanel/buildings')
    .then(response => response.json())
    .then(data => {
      setBuildings(data)
    });
  }, []);



  const Buildinglist = Object.values(buildings).map((building, index) =>{
    return (
            <tr key={index}>
                <td>
                <Link to={`/${building.name}/${building.id}`} target="_blank" rel="noopener noreferrer" params={{ building: building.name, address: building.address , id: building.id}}>
                    {building.name}
                </Link>
                </td>
                <td>{building.address}</td>
                <td>{building.id}</td>
            </tr>
    )
  })

  return (
      <div>
          <div className="ControlPanelTables">
            <p className="ControlPanelTableHeader" >Buildings</p>
            <table className="ControlPanelTable"> 
                <tbody>
                    <tr>
                        <th>Name</th>
                        <th>Address</th>
                        <th>ID</th>
                    </tr>
                    {Buildinglist}
                </tbody>
            </table>
          </div>
      </div>
        
  );

}
export default ControlBuildings