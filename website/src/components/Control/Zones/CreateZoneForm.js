import React, { useState, useEffect } from "react";



function CreateZoneForm(){
  const [zone, setZone] = useState({building: '', zone: ''})


  const inputChanged = (event) => {
    setZone({...zone, [event.target.name]: event.target.value});
  }

  function CreateZone(){
    //alert(`Building: ${building.name} At: ${building.address}`)
    fetch('/api/controlpanel/create/zone', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ building: zone.building, zone: zone.zone })
    }).then(response => response.json())
    .then(data => {
      if(data.result === "success"){
        alert("New zone created!")
      }
      else{
        alert("Something went wrong! Try again.")
      }
    })
    
    }

  return (
      <div className="CreateForm">
          <p>Create new zone</p>
        <div className="CreateFormForm">
            <input type="text" placeholder="BuildingName" name="building" value={zone.building} onChange={inputChanged} />
            <input type="text" placeholder="ZoneName" name="zone" value={zone.zone} onChange={inputChanged} />
            <button onClick={CreateZone}>Create</button>
          </div>
      </div>
        
  );

}
export default CreateZoneForm