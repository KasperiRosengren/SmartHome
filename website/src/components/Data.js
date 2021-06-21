import React from 'react';
import RealZone from './Visualization/RealZone';

let dataInParent = [
  {
      zone: "Kitchen",
      data: [{
              temperature: 
              {
                timestamp: ['05:00', '05:15', '05:30', '05:45'],
                values: [20, 24, 27, 36]
              }
            },
              { 
                humidity: 
                {
                    timestamp: ['05:00', '05:15', '05:30', '05:45'],
                    values: [20, 24, 27, 36]
                }
              },
                { 
                outlets: 
                  [
                    {name: "test", value:"on"},
                    {name: "test1", value:"on"},
                    {name: "test2", value:"on"},
                    {name: "test3", value:"on"}
                  ]
                }
            ]
  },
  {
      zone: "LivingRoom",
      data: [{
              temperature: 
              {
                  timestamp: ['05:00', '05:15', '05:30', '05:45'],
                  values: [20, 24, 27, 36]
              }},{ 
              humidity: 
              {
                  timestamp: ['05:00', '05:15', '05:30', '05:45'],
                  values: [20, 24, 27, 36]}
              },
              { 
              outlets: 
                [
                  {name: "test", value:"on"},
                  {name: "test1", value:"on"},
                  {name: "test2", value:"on"},
                  {name: "test3", value:"on"}
                ]
              }
            ]
  },
  {
      zone: "BedRoom",
      data: [{
              temperature: 
              {
                  timestamp: ['05:00', '05:15', '05:30', '05:45'],
                  values: [20, 24, 27, 36]
              }},{ 
              humidity: 
              {
                  timestamp: ['05:00', '05:15', '05:30', '05:45'],
                  values: [20, 24, 27, 36]}
              },
              { 
              outlets: 
                [
                  {name: "test", value:"on"},
                  {name: "test1", value:"on"},
                  {name: "test2", value:"on"},
                  {name: "test3", value:"on"}
                ]
              }
            ]
  }
]


let listzone = Object.keys(dataInParent).map((zone, index)=>{
  return <RealZone dataTo={dataInParent[index]} key={index} />
})

export default class Data extends React.Component {
  render() {
    return (
      <div className="LayoutTestMain">
          {listzone}
      </div>
    );
  }
}
