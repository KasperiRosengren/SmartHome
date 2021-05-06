import React, { useState } from 'react';

function Mqtt(){
    const [mqtt, setmqtt] = useState({topic: '', message: ''});

    const inputChanged = (event) => {
        setmqtt({...mqtt, [event.target.name]: event.target.value});
      }

    function sendMqtt(){
        fetch('/mqtt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          topic: mqtt.topic,
          message: mqtt.message
        })
      })
    }

    return (
        <div className="MqttPageMain">
            <input placeholder="Topic" name="topic" value={mqtt.topic} onChange={inputChanged} />
            <input placeholder="Message" name="message" value={mqtt.message} onChange={inputChanged}/>
            <button onClick={sendMqtt}>Send</button>
        </div>
      );
}

export default Mqtt