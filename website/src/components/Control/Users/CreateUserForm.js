import React, { useState, useEffect } from "react";



function CreateUserForm(){
  const [user, setUser] = useState({name: '', password: ''})


  const inputChanged = (event) => {
    setUser({...user, [event.target.name]: event.target.value});
  }

  function CreateUser(){
    //alert(`Building: ${building.name} At: ${building.address}`)
    fetch('/api/controlpanel/create/user', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: user.name, password: user.password })
    }).then(response => response.json())
    .then(data => {
      if(data.result === "success"){
        alert("New user created!")
      }
      else{
        alert("Something went wrong! Try again.")
      }
    })
    
    }

  return (
      <div className="CreateForm">
          <p>Create new user</p>
        <div className="CreateFormForm">
            <input type="text" placeholder="Username" name="name" value={user.name} onChange={inputChanged} />
            <input type="password" placeholder="Password" name="password" value={user.password} onChange={inputChanged}/>
            <button onClick={CreateUser}>Create</button>
          </div>
      </div>
        
  );

}
export default CreateUserForm