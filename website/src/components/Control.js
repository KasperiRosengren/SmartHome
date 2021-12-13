import React, { useState, useEffect } from "react";
import Buildings from './Control/Buildings/Buildings'
import Zones from "./Control/Zones/Zones";
import Devices from "./Control/Devices/Devices";
import Roles from "./Control/Roles/Roles";
import Users from "./Control/Users/Users";

function Control(){
    return (
        <div className="ControlPanelOuterDiv">
          <div className="ControlPanelInnerDiv"><Buildings /></div>
          <div className="ControlPanelInnerDiv"><Zones /></div>
          <div className="ControlPanelInnerDiv"><Devices /></div>
          <div className="ControlPanelInnerDiv"><Roles /></div>
          <div className="ControlPanelInnerDiv"><Users /></div>
        </div>
    );

}
export default Control