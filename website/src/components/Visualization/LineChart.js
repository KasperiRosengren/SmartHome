import React from 'react';
import {Line} from 'react-chartjs-2';

const state = {
  labels: ['05:00', '05:15', '05:30', '05:45',
            '06:00', '06:15', '06:30', '06:45',
            '07:00', '07:15', '07:30', '07:45'],
  datasets: [
    {
      label: 'Temperature',
      fill: false,
      lineTension: 0.5,
      backgroundColor: 'rgba(75,192,192,1)',
      borderColor: 'rgba(75,192,192,1)',
      borderWidth: 2,
      data: [65, 59, 80, 81, 56, 20, 43, 89, 15, 55, 67, 86]
    },{
        label: 'Humidity',
        fill: false,
        lineTension: 0.5,
        backgroundColor: 'rgba(165, 188, 71, 1)',
        borderColor: 'rgba(165, 188, 71, 1)',
        borderWidth: 2,
        data: [20, 24, 27, 36, 20, 14, 43, 70, 67, 62, 66, 58]
    }
  ]
}


export default class LineChart extends React.Component {
  render() {
    return (
      <div className="chart">
        <p className="chart_title">Kitchen</p>
        <Line data={state} />
      </div>
    );
  }
}

