import React from 'react';
import './App.css';
import Home from './components/Home';
import About from './components/About';
import Devices from './components/Devices';
import DataTest from './components/DataTest';
import Temperatures from './components/Data/Visuals/Weather/Charts/Temperatures';

//import io from 'socket.io-client'

import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';

function App() {
  return (
    <div className="PageMain">
      <BrowserRouter>
        <div className="NavBar">
          <ul className="TopNavList">
            <li className="TopNavItem"> <Link to="/"> Home </Link>{' '}</li>
            <li className="TopNavItem"> <Link to="/about"> About </Link>{' '}</li>
            <li className="TopNavItem"> <Link to="/devices"> Devices </Link>{' '}</li>
            <li className="TopNavItem"> <Link to="/datatest"> DataTest </Link>{' '}</li>
          </ul>
        </div>
        <div className="PageContent">
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/devices" component={Devices} />
            <Route path="/datatest" component={DataTest} />
            <Route path="/:buildingName/:zoneName/weather/temperature/all" component={Temperatures} />
          </Switch>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
