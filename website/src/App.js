import React from 'react';
import './App.css';
import Home from './components/Home';
import Devices from './components/Devices';
import Control from './components/Control';
import Temperatures from './components/Data/Visuals/Weather/Charts/Temperatures';
import ControlBuildings from './components/Control/Buildings/ControlBuildings';
import ControlBuilding from './components/Control/Buildings/ControlBuilding';


import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';

function App() {
  return (
    <div className="PageMain">
      <BrowserRouter>
        <div className="NavBar">
          <ul className="TopNavList">
            <li className="TopNavItem"> <Link to="/"> Home </Link>{' '}</li>
            

            <li className="TopNavItem"> <Link to="/devices"> Devices </Link>{' '}</li>
            <li className="TopNavItem"> <Link to="/control"> Control </Link>{' '}</li>
          </ul>
        </div>
        <div className="PageContent">
          <Switch>
            <Route exact path="/" component={Home} />
            

            <Route path="/devices" component={Devices} />
            <Route path="/control" component={Control} />
            <Route path="/:buildingName/:zoneName/weather/temperature/all" component={Temperatures} />
            <Route path="/buildings" component={ControlBuildings} />
            <Route path="/:buildingName/:buildingID" component={ControlBuilding}/>
          </Switch>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
