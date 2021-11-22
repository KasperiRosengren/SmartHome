import React, { useState, useEffect } from "react";
import CreateRoleForm from "./CreateRoleForm";


function Roles(){
  const [roles, setRoles] = useState([])


  useEffect(() => {
    fetch('/api/get/controlpanel/roles')
    .then(response => response.json())
    .then(data => {
        setRoles(data)
    });
  }, []);



  const Rolelist = Object.values(roles).map((role, index) =>{
    return (
    <tr key={index}>
        <td>{role.name}</td>
        <td>{role.id}</td>
    </tr>
    )
  })

  return (
      <div>
        <p className="ControlPanelTableHeader">Roles</p>
        <table className="ControlPanelTable"> 
            <tbody>
                <tr>
                    <th>Role Name</th>
                    <th>ID</th>
                </tr>
                {Rolelist}
            </tbody>
        </table>
        <CreateRoleForm />
      </div>
        
  );

}
export default Roles