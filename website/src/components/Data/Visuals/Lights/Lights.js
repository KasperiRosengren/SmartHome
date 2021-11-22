import React, { useState, useEffect} from 'react';
import NewLight from './NewLight';
import Light from './Light';

const Lights = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [buildingName, setBuildingName] = useState(props.building)
    const [lights, setLights] = useState([props.info])

    let lightlist = lights.map((light, index)=>{
        //console.log(light)
        if(Object.entries(light).length !== 0){
            if(light.lights.hasOwnProperty('light_0') || light.lights.hasOwnProperty('light_1')){
                //console.log("Here was a light")
                return(
                    Object.entries(light.lights).map((thisLight, thisIndex)=>{
                        console.log(thisLight)
                        return(
                            <div className="light">
                                <Light
                                    key={thisIndex} 
                                    zone={zoneName}
                                    building={buildingName}
                                    originalName={thisLight[0]}
                                    info={thisLight[1]}
                                /> 
                            </div>    
                        )
                    })
                    
                )
            }
        }
    })
            
        
    
   return(
       <div className="lightOuter">
           {lightlist}
       </div>
   )
}

export default Lights
