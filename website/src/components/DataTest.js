import React, { useState, useEffect } from "react";
import Zone from "./Data/Zone";
//import RealZone from './Visualization/RealZone';



function DataTest(){
  const [buildings, setBuildings] = useState([])


  useEffect(() => {
    fetch('/api/get/frontend/test/init')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setBuildings(data)
    });
  }, []);


  //useEffect(() => console.log(buildings), [buildings]);



  const zonelist = Object.keys(buildings).map((building, index) =>{
    return <Zone dataTo={buildings[building]} key={index}/>
  })

  return (
    <div className="LayoutTestMain">
      {zonelist}
    </div>
  );

  /*
  const buildinglist = Object.keys(buildings).map((building, index) =>{
    console.log(buildings[building].outlets);
    <tr key={index}>
      <td>{buildings[building].Building}</td>
      <td>{buildings[building].Zone}</td>
      <td>{buildings[building].ZoneID}</td>
    </tr>
  })

  return (
    <div className="LayoutTestMain">
      <table style={{width: "60%"}}>
        <tr>
          <th style={{padding: "15px"}}>Building</th>
          <th style={{padding: "15px"}}>Zone</th>
          <th style={{padding: "15px"}}>ID</th>
        </tr>
          {buildinglist}
      </table>
        <p>checklog</p>
    </div>
  );
  */
}
export default DataTest