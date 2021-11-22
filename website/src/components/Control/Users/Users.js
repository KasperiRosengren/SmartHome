import React, { useState, useEffect } from "react";
import CreateUserForm from "./CreateUserForm";



function Users(){
  const [users, setUsers] = useState([])


  useEffect(() => {
    fetch('/api/get/controlpanel/users')
    .then(response => response.json())
    .then(data => {
        setUsers(data)
    });
  }, []);



  const Rolelist = Object.values(users).map((user, index) =>{
    return (
    <tr key={index}>
        <td>{user.username}</td>
        <td>{user.id}</td>
    </tr>
    )
  })

  return (
      <div>
        <p className="ControlPanelTableHeader">Users</p>
        <table className="ControlPanelTable"> 
            <tbody>
                <tr>
                    <th>Username</th>
                    <th>ID</th>
                </tr>
                {Rolelist}
            </tbody>
        </table>
        <CreateUserForm />
      </div>
        
  );

}
export default Users