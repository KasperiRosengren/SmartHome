import React, { useState, useEffect} from 'react';
import Light from './Light';

const LightOpener = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [buildingName, setBuildingName] = useState(props.building)
    const [lights, setLights] = useState([props.info])
    const [originalName, setOriginalName] = useState(props.originalName)

    let lightlist = lights.map((light, index)=>{
        console.log(light)
        console.log(originalName)
        return(
            <div>
                <Light key={index}
                    info={light}
                    building={buildingName}
                    zone={zoneName}
                    originalName={originalName} />
            </div>
        )
    })
            
        
    
   return(
       <div>
           {lightlist}
       </div>
   )
}

export default LightOpener
