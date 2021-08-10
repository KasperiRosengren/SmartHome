import React, { useState, useEffect, useRef} from 'react';
import {Line} from 'react-chartjs-2';
import io from 'socket.io-client'

const ChartLine = props =>{
  const [temp, setTemp] = useState(props.temp)
  const [hum, setHum] = useState(props.hum)
  const [tst, setTst] = useState(props.tst)

  const zone = props.zone
  
  const [state, setState] = useState({
      labels: tst,
      datasets: [
        {
          label: 'Temperature',
          fill: false,
          lineTension: 0.5,
          backgroundColor: 'rgba(75,192,192,1)',
          borderColor: 'rgba(75,192,192,1)',
          borderWidth: 2,
          data: temp
        },{
            label: 'Humidity',
            fill: false,
            lineTension: 0.5,
            backgroundColor: 'rgba(165, 188, 71, 1)',
            borderColor: 'rgba(165, 188, 71, 1)',
            borderWidth: 2,
            data: hum
        }
      ]
    })
    const ref = useRef();
    useEffect(() => {
      const socket = io("http://localhost:5000/");
      //console.log(socket)
      socket.emit('tester', 'working!')
      socket.emit('join', {username: zone+'User', room: zone})

      socket.on("roomData", (data) => {
        console.log('new data: ', data)
        
        setHum([...hum, data.hum])
        setTemp([...temp, data.temp])
        setTst([...tst, data.tst])
        
        let newState = state
        newState.labels.push(data.tst)
        newState.datasets[0].data.push(data.temp)
        newState.datasets[1].data.push(data.hum)
        setState(newState)
        
        //let { temperature, newData} = temperature
        console.log(state)
        //ref.update()
      });
    }, [])


  return(
      <div>
          <Line data={state} ref={ref}/>
      </div>
  )
}

export default ChartLine