import React, { useState, useEffect} from 'react';
import Temperature from './Temperature';
import Humidity from './Humidity';
//import Airpressure from './Airpressure';


const Weather = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [buildingName, setBuildingName] = useState(props.building)
    const [weather, setWeather] = useState([props.info])

    let weatherlist = weather.map((weat, index)=>{
        //console.log(weat)
        return(
            <div key={index} className="thermgauge">
                <Temperature data={weat.temperature} zone={zoneName} building={buildingName}/>
                <Humidity data={weat.humidity} />
            </div>
        )
    })
            //<Airpressure data={weat.airpressure} />
        
    
   return(
       <div>
           {weatherlist}
       </div>
   )
}

export default Weather
