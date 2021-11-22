import React, { useState, useEffect } from "react";
import CreateDeviceForm from "./CreateDeviceForm";



function Devices(){
  const [devices, setDevices] = useState([])


  useEffect(() => {
    fetch('/api/get/controlpanel/devices')
    .then(response => response.json())
    .then(data => {
      setDevices(data)
    });
  }, []);



  const Devicelist = Object.values(devices).map((device, index) =>{
    return (
    <tr key={index}>
        <td>{device.buildingname}</td>
        <td>{device.zonename}</td>
        <td>{device.devicename}</td>
        <td>{device.id}</td>
    </tr>
    )
  })

  return (
      <div>
        <p className="ControlPanelTableHeader">Devices</p>
        <table className="ControlPanelTable"> 
            <tbody>
                <tr>
                    <th>Building Name</th>
                    <th>Zone Name</th>
                    <th>Device Name</th>
                    <th>ID</th>
                </tr>
                {Devicelist}
            </tbody>
        </table>
        <CreateDeviceForm />
      </div>
        
  );

}
export default Devices