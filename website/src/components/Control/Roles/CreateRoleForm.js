import React, { useState, useEffect } from "react";



function CreateRoleForm(){
  const [role, setRole] = useState({name: ''})


  const inputChanged = (event) => {
    setRole({...role, [event.target.name]: event.target.value});
  }

  function CreateRole(){
    //alert(`Building: ${building.name} At: ${building.address}`)
    fetch('/api/controlpanel/create/role', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: role.name})
    }).then(response => response.json())
    .then(data => {
      if(data.result === "success"){
        alert("New role created!")
      }
      else{
        alert("Something went wrong! Try again.")
      }
    })
    
    }

  return (
      <div className="CreateForm">
          <p>Create new role</p>
        <div className="CreateFormForm">
            <input type="text" placeholder="RoleName" name="name" value={role.name} onChange={inputChanged} />
            <button onClick={CreateRole}>Create</button>
          </div>
      </div>
        
  );

}
export default CreateRoleForm