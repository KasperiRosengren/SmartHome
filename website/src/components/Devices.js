import React, { useState, useEffect } from "react";
import Zone from "./Data/Zone";
//import RealZone from './Visualization/RealZone';



function Devices(){
  const [buildings, setBuildings] = useState([])


  useEffect(() => {
    fetch('/api/get/frontend/init')
    .then(response => response.json())
    .then(data => {
      if(data.result !== "failure"){
        console.log(data)
        setBuildings(data)
      }
      else{
        console.log(data)
      }
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
}
export default Devices