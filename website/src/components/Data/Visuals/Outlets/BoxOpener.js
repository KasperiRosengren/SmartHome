import React, { useState, useEffect} from 'react';
import Outlet from './Outlet';



const BoxOpener = props =>{
    const [zoneName, setZoneName] = useState(props.zone)
    const [outletboxes, setOutletBoxes] = useState([props.info])
/*
    let outletlist = outletboxes.map((outletbox, index)=>{
        console.log(outletbox)
        console.log(outletbox[0])
        return(
            Object.entries(outletbox[1].outlets).map((outlet, outletindex)=>{
                console.log(outlet)
                return(<p key={outletindex}>Outlet</p>)
            })
        )
    })
*/

    let outletlist = outletboxes.map((outletbox, index)=>{
        //console.log(outletbox)
        //console.log(outletbox[0])
        return(
            Object.entries(outletbox[1].outlets).map((outlet, outletindex)=>{
                //console.log(outlet)
                return(<Outlet key={outletindex}
                    outletoriginal={outlet[0]}
                    box={outletbox[0]}
                    name={outlet[1].name}
                    zone={zoneName}
                    value={outlet[1].status}/>)
            })
        )
    })
   return(
       <div className="outlets">
           {outletlist}
       </div>
   )
}

export default BoxOpener
