import React, { useState, useEffect} from 'react';

const buttonStyleOn = { color: 'black', backgroundColor: 'white' };
const buttonStyleOff = { color: 'white', backgroundColor: 'black' };


const Outlet = props =>{
    const [outlet, setOutlet] = useState({name: props.name, value: props.value})
    //console.log(props.zone)
    if(outlet.value === "on"){
        return (
            <div className="outlet">
                <button
                    type="submit"
                    style={buttonStyleOn}
                    onClick={turnOff => { 
                        fetch('/api/control/device/outlet/status', {
                            method: 'POST',
                            headers: {
                              'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({building:props.zone.building, zone: props.zone.zone, box: props.box, name: props.outletoriginal, command: "off" })
                            })
                            .then(response => response.json())
                            .then(data => {
                                if(data.result === "success"){
                                    setOutlet({...outlet, value: "off"})
                                }
                            })
                        }}>
                    {outlet.name}
                </button>
            </div>
        );
    }
    else{
        return (
            <div className="outlet">
                <button
                    type="submit"
                    style={buttonStyleOff}
                    onClick={turnOn => { 
                        fetch('/api/control/device/outlet/status', {
                            method: 'POST',
                            headers: {
                              'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({building:props.zone.building, zone: props.zone.zone, box: props.box, name: props.outletoriginal, command: "on" })
                            })
                            .then(response => response.json())
                            .then(data => {
                                if(data.result === "success"){
                                    setOutlet({...outlet, value: "on"})
                                }
                            })
                        }}>
                    {outlet.name}
                </button>
            </div>
        );
    }
    
}

export default Outlet
