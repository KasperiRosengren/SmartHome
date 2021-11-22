import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import CreateBuildingForm from "./CreateBuildingForm";


function Building(){
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
        <td><Link to={`/${building.name}`} target="_blank" rel="noopener noreferrer" params={{ building: building.name, address: building.address , id: building.id}}>
          {building.name}
        </Link></td>
        <td><Link to={`/${building.name}`} target="_blank" rel="noopener noreferrer" params={{ building: building.name, address: building.address , id: building.id}}>
          {building.address}
        </Link></td>
        <td><Link to={`/${building.name}`} target="_blank" rel="noopener noreferrer" params={{ building: building.name, address: building.address , id: building.id}}>
          {building.id}
        </Link></td>
    </tr>
    )
  })

  return (
      <div>
        <Link to={`/buildings`} target="_blank" rel="noopener noreferrer">
          <p className="ControlPanelTableHeader" >Buildings</p>
        </Link>
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
        <div className="ControlPanelForm"><CreateBuildingForm /></div>
        
      </div>
        
  );

}
export default Building