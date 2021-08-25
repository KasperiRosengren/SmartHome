import React, { useState, useEffect, useRef} from 'react';
import {Line} from 'react-chartjs-2';
//import io from 'socket.io-client'

const DailyChart = props =>{
  const [data, setData] = useState(props.data)


  const deviceName = props.deviceName
  const building = props.building
  const zone = props.zone
  
  console.log("min: " + data.time[data.time.length - 1])
  console.log("max: " + data.time[0])
  const [state, setState] = useState({
      labels: data.time,
      datasets: [
        {
          label: `${building}/${zone}/${deviceName}`,
          fill: false,
          lineTension: 0.5,
          backgroundColor: 'rgba(75,192,192,1)',
          borderColor: 'rgba(75,192,192,1)',
          borderWidth: 2,
          data: data.values
        }
      ]
    })

    const ref = useRef();


  return(
      <div style={{marginLeft: "2%", marginRight: "2%"}}>
          <Line data={state} ref={ref} />
      </div>
  )
}

export default DailyChart