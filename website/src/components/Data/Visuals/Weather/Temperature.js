import React, { useState, useEffect} from 'react';
import Thermometer from 'react-thermometer-component'
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';
import Temperatures from './Charts/Temperatures';


const Temperature = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [buildingName, setBuildingName] = useState(props.building)
    const [weather, setWeather] = useState([props.data])





    let weatherlist = Object.entries(weather).map((weat, index)=>{
        return(
            Object.values(JSON.parse(weat[1])).map((temperature, index)=>{
                if(temperature.temperature.hasOwnProperty('value')){
                    return(
                        <div>
                            <Link to={`/${buildingName}/${zoneName}/weather/temperature/all`} target="_blank" rel="noopener noreferrer" params={{ building: buildingName, zone: zoneName}}>
                                <Thermometer
                                    theme="dark"
                                    value={temperature.temperature.value}
                                    max="50"
                                    steps="5"
                                    format="°C"
                                    size="large"
                                    height="400"
                                />
                            </Link>
                        </div>
                    )
                }
            })
            
        )
    })
            
    //<Redirect push to="http://localhost:3000/:buildingName/:zoneName+/weather/temperature/all" />
    //<div  onClick={()=>window.open("http://localhost:3000/"+buildingName+"/"+zoneName+"/weather/temperature/all")}></div>
    
   return(
       <div className="thermgaugeinside">

           {weatherlist}
       </div>
   )
}

export default Temperature
