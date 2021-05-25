import React from 'react';

function Data(){
  var isLoggedin = localStorage.getItem('isLoggedin')

  if(isLoggedin === "1"){
    return (
      <div className="HomePageMain">
        <p>NUMBERSSSSSS! {isLoggedin}</p>
      </div>
    );
  }
  else{
    return (
      <div className="HomePageMain">
        <p>COLORSSS! {isLoggedin}</p>
      </div>
    );
  }
}

export default Data