import React, { useState, useEffect} from 'react';
import Outlet from './Outlet';
import BoxOpener from './BoxOpener';



const OutletBox = props =>{
    //const [zoneName, setZoneName] = useState({name: props.building + "/" + props.zone})
    const [zoneName, setZoneName] = useState({building: props.building, zone: props.zone})
    const [outletboxes, setOutletBoxes] = useState([props.info])


    let outletboxlist = outletboxes.map((outletbox, index)=>{
        //console.log(Object.entries(outletbox).length)
        if(Object.entries(outletbox).length !== 0)
        {
            if(outletbox.hasOwnProperty('outletbox_0')){
                /*
                console.log(outletbox)
                console.log(outletbox.outletbox_0)
                console.log(outletbox.outletbox_0.name)
                console.log(outletbox.outletbox_0.outlets)
                console.log(outletbox.outletbox_1)
                console.log(outletbox.outletbox_1.outlets)
                */
                return(
                    Object.entries(outletbox).map((thisBox, thisIndex)=>{
                        //console.log(thisBox)
                        return(
                            <div>
                                <BoxOpener key={thisIndex} info={thisBox} zone={zoneName}/>
                            </div>
                        )
                    })
                )
            }
        }
        
    })


   return(
       <div className="outletBoxes">
           {outletboxlist}
       </div>
   )
}

export default OutletBox
