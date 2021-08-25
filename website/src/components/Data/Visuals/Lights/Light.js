import React, { useState, useEffect} from 'react';

const Light = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [buildingName, setBuildingName] = useState(props.building)
    const [light, setLight] = useState({name: props.info.name,
                                        status: props.info.status, 
                                        pattern: props.info.pattern, 
                                        color_0: props.info.color_0, 
                                        color_1: props.info.color_1, 
                                        color_2: props.info.color_2})
    const [buttonStyle, setButtonStyle] = useState({ color: 'white', backgroundColor: 'black' })
    

    useEffect(() => {
        if(light.status==="off"){
            setButtonStyle({ color: 'white', backgroundColor: 'black', height: "25px", width: "100px", fontSize: "1rem"  })
        }else{
            setButtonStyle({ color: 'black', backgroundColor: 'white', height: "25px", width: "100px", fontSize: "1rem"  })
        }
        
    }, [])
        console.log(light)

    const redButtonStyle=({ backgroundColor: "red", height: "25px", width: "25px" })
    const greenButtonStyle=({ backgroundColor: "green", height: "25px", width: "25px" })
    const blueButtonStyle=({ backgroundColor: "blue", height: "25px", width: "25px" })

    return(
        <div>
            <p>Name: {light.name}</p>
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
            <button type="submit" style={{ color: 'white', backgroundColor: 'black', fontSize: "1rem"  }}
                onClick={changePatternAllSame => {
                    fetch('/api/control/device/light/pattern',{
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                            pattern: "allsame" })})
                        .then(response => response.json())
                        .then(data => { if(data.result === "success"){ setLight({...light, pattern: "allsame"}) }})
            }} >all same</button>

            <button type="submit" style={{ color: 'white', backgroundColor: 'black', fontSize: "1rem"  }}
                onClick={changePatternAllSame => {
                    fetch('/api/control/device/light/pattern',{
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                            pattern: "chase" })})
                        .then(response => response.json())
                        .then(data => { if(data.result === "success"){ setLight({...light, pattern: "chase"}) }})
            }} >chase</button>

            <button type="submit" style={{ color: 'white', backgroundColor: 'black', fontSize: "1rem" }}
                onClick={changePatternAllSame => {
                    fetch('/api/control/device/light/pattern',{
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                            pattern: "backandforth" })})
                        .then(response => response.json())
                        .then(data => { if(data.result === "success"){ setLight({...light, pattern: "backandforth"}) }})
            }} >backandforth</button>



            <p>Color 1: {light.color_0}</p>
                <button type="submit"
                    style={redButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_0", newColor: "red" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_0: "red"}) }})
                    }} ></button>

                <button type="submit"
                    style={greenButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_0", newColor: "green" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_0: "green" }) }})
                    }} ></button>

                <button type="submit"
                    style={blueButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_0", newColor: "blue" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_0: "blue" }) }})
                    }} ></button>
            <p>Color 2: {light.color_1}</p>

            <button type="submit"
                    style={redButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_1", newColor: "red" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_1: "red"}) }})
                    }} ></button>

                <button type="submit"
                    style={greenButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_1", newColor: "green" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_1: "green" }) }})
                    }} ></button>

                <button type="submit"
                    style={blueButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_1", newColor: "blue" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_1: "blue" }) }})
                    }} ></button>


            <p>Color 3: {light.color_2}</p>

            <button type="submit"
                    style={redButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_2", newColor: "red" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_2: "red"}) }})
                    }} ></button>

                <button type="submit"
                    style={greenButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_2", newColor: "green" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_2: "green" }) }})
                    }} ></button>

                <button type="submit"
                    style={blueButtonStyle}
                    onClick={changeColor_0Red => {
                        fetch('/api/control/device/light/color',{
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({building:props.building, zone: props.zone, name: props.originalName,
                                color: "color_2", newColor: "blue" })})
                            .then(response => response.json())
                            .then(data => { if(data.result === "success"){ setLight({...light, color_2: "blue" }) }})
                    }} ></button>
        </div>
    
   )
}

export default Light
