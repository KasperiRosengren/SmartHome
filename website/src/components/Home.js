import React, { useState } from 'react';

function Home(){
  const [isLoggedin, setIsLoggedin] = useState("");
  if(!localStorage.getItem('isLoggedin')) {
    localStorage.setItem('isLoggedin', "0");
    setIsLoggedin("0")
  }
  const [user, setUser] = useState({username: '', password: ''});
  
  const inputChanged = (event) => {
    setUser({...user, [event.target.name]: event.target.value});
  }

  function sendLogin(){
    fetch('/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username: user.username, password: user.password })
    }).then(response => response.json())
    .then(data => {
      if(data.result === "success"){
        localStorage.setItem('isLoggedin', "1");
        setIsLoggedin("1");
      }
    })
  }

  function getInfo(){
    fetch('/api/auth/whoami').then(res => res.json()).then(data => {
      alert("Hello:" + data.name + "\nYour id is:" + data.id)
    });
  }

  function logout(){
    fetch('/api/auth/logout').then(res => res.json()).then(data => {
      if(data.result === "success"){
        localStorage.setItem('isLoggedin', "0");
        setIsLoggedin("0");
      }
    });
  }

  if(isLoggedin === "1"){
    return(
      <div className="HomePageMain">
        <button onClick={getInfo}>GET</button>
        <button onClick={logout}>LOGOUT</button>
      </div>
    )
  }
  else{
    return (
      <div className="HomePageMain">
        <p>This is our nice home page for SaMi</p>
        <h1>Login</h1>
          <div>
            <input type="text" placeholder="Username" name="username" value={user.username} onChange={inputChanged} />
            <input type="password" placeholder="Password" name="password" value={user.password} onChange={inputChanged}/>
            <button onClick={sendLogin}>Send</button>
          </div>

        </div>
    );
  }
}

export default Home