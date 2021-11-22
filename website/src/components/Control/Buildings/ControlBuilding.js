import React, { useState, useEffect } from "react";



const ControlBuilding = props =>{
  const [buildings, setBuildings] = useState([])

  console.log(props.match.params)
  console.log(props.match.params.buildingName)
  console.log(props)


  return (
      <div>
          hello
      </div>
        
  );

}
export default ControlBuilding