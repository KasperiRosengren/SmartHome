import React, { useEffect, useState} from 'react';

const colorPickerStyleRed = {
    color: 'black',
    backgroundColor: 'red'
}

const colorPickerStyleBlue = {
    color: 'black',
    backgroundColor: 'blue'
}

const colorPickerStyleGreen = {
    color: 'black',
    backgroundColor: 'green'
}

/*
export default class Light extends React.Component {
    render() {
        let patternlist = this.props.info.patterns.map((pattern, index)=>{
            return <div className="pattern"  key={index}>{pattern}</div>
        })
        return(
            <div className="leds">
                <div className="info">
                    <div className="ledName">{this.props.info.name}</div>
                    <div className="patterns">
                        {patternlist}
                    </div>
                </div>
                <div className="colorpicker">
                    <div style={colorPickerStyleRed}>red</div>
                    <div style={colorPickerStyleBlue}>blue</div>
                    <div style={colorPickerStyleGreen}>green</div>
                </div>
            </div>
        )
    }
}

*/

const Light = props =>{
    const [light, setLight] = useState({name: props.info.name, patterns: props.info.patterns})
    const [selected, setSelected] = useState({pattern: props.info.statusPattern, color: props.info.statusValue})
    const colorWheel = ['red', 'green', 'blue', 'yellow', 'black']

    let colorlist = colorWheel.map((colorName, index)=>{
        return <button
                className="colorbox"
                style={{backgroundColor: colorName}}
                onClick={sendColor => { 
                    fetch('/api/new/test1', {
                        method: 'POST',
                        headers: {
                          'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ zone: props.zone, name: light.name, color: selected.color })
                        })
                        .then(response => response.json())
                        .then(data => {
                            if(data.result === "success"){
                                setSelected({...selected, color: colorName})
                            }
                        })
                    } }
                ></button>
    })

    let patternlist = light.patterns.map((patternName, index)=>{
        return <button
                className="pattern"
                type="submit"
                key={index}
                onClick={sendPattern => { 
                    fetch('/api/new/test2', {
                        method: 'POST',
                        headers: {
                          'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ zone: props.zone, name: light.name, pattern: selected.pattern })
                        })
                        .then(response => response.json())
                        .then(data => {
                            if(data.result === "success"){
                                setSelected({...selected, pattern: patternName})
                            }
                        })
                    } }
                >{patternName}</button>
    })
    return(
        <div className="leds">
                <div className="info">
                    <div className="ledName">{light.name}/{selected.pattern}/{selected.color}</div>
                    <div className="patterns">
                        {patternlist}
                    </div>
                </div>
                <div className="colorpicker">
                    {colorlist}
                </div>
            </div>
    )
    
}

export default Light