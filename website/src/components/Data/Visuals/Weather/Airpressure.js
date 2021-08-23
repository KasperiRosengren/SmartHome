import React, { useState, useEffect} from 'react';
import Thermometer from 'react-thermometer-component'



const Airpressure = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [weather, setWeather] = useState([props.data])

    let weatherlist = Object.entries(weather).map((weat, index)=>{
        return(
            Object.values(JSON.parse(weat[1])).map((airpressure, index)=>{
                if(airpressure.airpressure.hasOwnProperty('value')){
                    return(
                        <Thermometer
                            theme="dark"
                            value={airpressure.airpressure.value}
                            max="1200"
                            steps="6"
                            format="hPa"
                            size="large"
                            height="400"
                        />
                    )
                }
            })
            
        )
    })
            
        
    
   return(
       <div className="thermgaugeinside">
           {weatherlist}
       </div>
   )
}

export default Airpressure
