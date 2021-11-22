import React, { useState, useEffect } from "react";



function CreateBuildingForm(){
  const [building, setBuilding] = useState({name: '', address: ''})


  const inputChanged = (event) => {
    setBuilding({...building, [event.target.name]: event.target.value});
  }

  function CreateBuilding(){
    //alert(`Building: ${building.name} At: ${building.address}`)
    fetch('/api/controlpanel/create/building', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: building.name, address: building.address })
    }).then(response => response.json())
    .then(data => {
      if(data.result === "success"){
        alert("New building created!")
      }
      else{
        alert("Something went wrong! Try again.")
      }
    })
    
    }

  return (
      <div className="CreateForm">
          <p>Create new building</p>
        <div className="CreateFormForm">
            <input type="text" placeholder="BuildingName" name="name" value={building.name} onChange={inputChanged} />
            <input type="text" placeholder="Address" name="address" value={building.address} onChange={inputChanged}/>
            <button onClick={CreateBuilding}>Create</button>
          </div>
      </div>
        
  );

}
export default CreateBuildingForm