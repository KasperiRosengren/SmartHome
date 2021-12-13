import React, { useState, useEffect } from "react";



function CreateDeviceForm(){
  const [device, setDevice] = useState({building: '', zone: '', device: '', location: ''})


  const inputChanged = (event) => {
    setDevice({...device, [event.target.name]: event.target.value});
  }

  function CreateDevice(){
    //alert(`Building: ${building.name} At: ${building.address}`)
    fetch('/api/controlpanel/create/device', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ building: device.building, zone: device.zone, device: device.device, location: device.location })
    }).then(response => response.json())
    .then(data => {
      if(data.result === "success"){
        alert("New Device created!")
      }
      else{
        alert("Something went wrong! Try again.")
      }
    })
    
    }

  return (
      <div className="CreateForm">
          <h3>Create new device</h3>
        <div className="CreateFormForm">
            <input className="CreateFormInput" type="text" placeholder="BuildingName" name="building" value={device.building} onChange={inputChanged} />
            <input className="CreateFormInput" type="text" placeholder="ZoneName" name="zone" value={device.zone} onChange={inputChanged} />
            <input className="CreateFormInput" type="text" placeholder="DeviceName" name="device" value={device.device} onChange={inputChanged} />
            <input className="CreateFormInput" type="text" placeholder="Location" name="location" value={device.location} onChange={inputChanged}/>
            <button style={{fontSize: "2vh"}} onClick={CreateDevice}>Create</button>
          </div>
      </div>
        
  );

}
export default CreateDeviceForm