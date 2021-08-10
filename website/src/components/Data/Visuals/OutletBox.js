import React, { useState, useEffect} from 'react';
import Outlet from './Outlet';



const OutletBox = props =>{
    const [zoneNames, setZoneNames] = useState({name: props.building + "/" + props.zone})
    const [outlets, setOutlet] = useState(props.info)

    useEffect(() => console.log(outlets), [outlets]);
/*
    let outletlist = outlets.map((outlet, index)=>{
        return <p>{outlets[index]}</p>
        //return <Outlet info={outlets[index]} key={index}/>
      })
*/
      let zonelist = Object.keys(zoneNames).map((zonename, index)=>{
        return <p>{zoneNames[index].name}</p>
        //return <Outlet info={outlets[index]} key={index}/>
      })


   return(
       <div>
           
           {zonelist}
       </div>
   )
}

export default OutletBox
