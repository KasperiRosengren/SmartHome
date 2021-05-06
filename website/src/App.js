import React from 'react';
import './App.css';
import Home from './components/Home';
import About from './components/About';
import Data from './components/Data';
import Mqtt from './components/Mqtt';
import Mysql from './components/Mysql';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';


function App() {
  return (
    <div className="PageMain">
      <BrowserRouter>
        <div className="NavBar">
          <ul className="TopNavList">
            <li className="TopNavItem">
              <Link to="/"> Home </Link>{' '}
            </li>
            <li className="TopNavItem">
              <Link to="/about"> About </Link>{' '}
            </li>
            <li className="TopNavItem">
              <Link to="/data"> Data </Link>{' '}
            </li>
            <li className="TopNavItem">
              <Link to="/mqtt"> Mqtt </Link>{' '}
            </li>
            <li className="TopNavItem">
              <Link to="/mysql"> Mysql </Link>{' '}
            </li>
          </ul>
        </div>
        <div className="PageContent">
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/data" component={Data} />
            <Route path="/mqtt" component={Mqtt} />
            <Route path="/mysql" component={Mysql} />
          </Switch>
        </div>
      </BrowserRouter> 
    </div>
  );
}

export default App;
