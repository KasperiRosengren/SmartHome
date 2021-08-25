import React, { useState, useEffect } from 'react';

function About(){
    const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
    
  }, []);

    return (
        <div className="AboutPageMain">
            <h1>The current time is:</h1>
            <p>Year: {currentTime[0]}, Month {currentTime[2]}, Day: {currentTime[1]}</p>
            <p>Hour: {currentTime[3]}, Minute: {currentTime[4]}, Second: {currentTime[5]}</p>
        </div>
      );
}

export default About