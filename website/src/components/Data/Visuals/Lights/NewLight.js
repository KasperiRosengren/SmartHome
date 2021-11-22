import React, { useState, useEffect} from 'react';


const NewLight = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [buildingName, setBuildingName] = useState(props.building)
    const [light, setLight] = useState({name: props.info.name,
                                        status: props.info.status, 
                                        pattern: props.info.pattern, 
                                        color_0: props.info.color_0, 
                                        color_1: props.info.color_1, 
                                        color_2: props.info.color_2})
    const [buttonStyle, setButtonStyle] = useState({ color: 'white', backgroundColor: 'black' })
    
    const [color_0, setColor_0] = useState(props.info.color_0)
    const [color_1, setColor_1] = useState(props.info.color_1)
    const [color_2, setColor_2] = useState(props.info.color_2)


    useEffect(() => {
        if(light.status==="off"){
            setButtonStyle({ color: 'white', backgroundColor: 'black', height: "5vh", width: "20vh", fontSize: "3vh"  })
        }else{
            setButtonStyle({ color: 'black', backgroundColor: 'white', height: "25px", width: "100px", fontSize: "4vh"  })
        }
        
    }, [])
    //console.log(light)

    const redButtonStyle=({ backgroundColor: "red", height: "25px", width: "25px" })
    const greenButtonStyle=({ backgroundColor: "green", height: "25px", width: "25px" })
    const blueButtonStyle=({ backgroundColor: "blue", height: "25px", width: "25px" })
    /*
            <p>Name:</p>
            <p>{light.name}</p>
    */

    return(
        <div className="light">
            <button
                    type="submit"
                    style={buttonStyle}
                    onClick={changeStatus => { 
                        fetch('/api/control/device/light/status',{
                            method: 'POST',
                            headers: {
                              'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName, status: light.status })
                            })
                            .then(response => response.json())
                            .then(data => {
                                if(data.result === "success"){
                                    if(light.status==="off"){
                                        setLight({...light, status: "on"})
                                        setButtonStyle({ color: 'black', backgroundColor: 'white', height: "25px", width: "100px", fontSize: "1rem"  })
                                    }
                                    else{
                                        setLight({...light, status: "off"})
                                        setButtonStyle({ color: 'white', backgroundColor: 'black', height: "25px", width: "100px", fontSize: "1rem"  })
                                    }
                                }
                            })
                        }}>
                    {light.name}
                </button>
            <p>Pattern: {light.pattern}</p>
            <p>Color 1: {color_0}</p>
            <p>Color 2: {color_1}</p>
            <p>Color 3: {color_2}</p>
            
        </div>
    
   )
}

export default NewLight
