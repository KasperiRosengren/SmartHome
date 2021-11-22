import React, { useState, useEffect} from 'react';
import Thermometer from 'react-thermometer-component'



const Humidity = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [weather, setWeather] = useState([props.data])

    let weatherlist = Object.entries(weather).map((weat, index)=>{
        return(
            Object.values(JSON.parse(weat[1])).map((humidity, index)=>{
                if(humidity.humidity.hasOwnProperty('value')){
                    return(
                        <div className="thermgaugeInner">
                            <div>
                                <Thermometer
                                    theme="dark"
                                    value={humidity.humidity.value}
                                    max="100"
                                    steps="5"
                                    format="%"
                                    size="large"
                                    height="400"
                                />
                            </div>
                            <div className="thermgaugeText">
                                <p>Hum.</p>
                                <p>{humidity.humidity.value} %</p>
                            </div>
                            </div>


                        
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

export default Humidity
