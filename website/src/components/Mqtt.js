import React, { useEffect, useState } from 'react';

function Mqtt(){
    const [mqtt, setmqtt] = useState({topic: 'test', message: 'test'});
    const [topics, setTopics] = useState([])

    const inputChanged = (event) => {
        setmqtt({...mqtt, [event.target.name]: event.target.value});
      }

    function sendMqtt(){
        fetch('/api/mqtt/send/message', {
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


    useEffect(() => {
      const interval = setInterval(() => {
        fetch('/api/mqtt/get/message/all')
        .then(response => response.json())
        .then(data => setTopics(data))
        .catch(error=>{
          console.log(error)
        })
      }, 2000);
      return () => clearInterval(interval);
    }, []);
    
/*
    function mqttGetMessageAll(){
      fetch('/api/mqtt/get/message/all')
      .then(response => response.json())
      .then(data => setTopics(data))
      .catch(error=>{
        console.log(error)
      })
      setTimeout(mqttGetMessageAll, 2000)
    }

    setTimeout(mqttGetMessageAll, 2000)


    setInterval(function(){
      fetch('/api/mqtt/get/message/all')
      .then(response => response.json())
      .then(data => setTopics(data))
      .catch(error=>{
        console.log(error)
      })
    }, 2000)
*/

    return (
        <div className="MqttPageMain">
            <input placeholder="Topic" name="topic" value={mqtt.topic} onChange={inputChanged} />
            <input placeholder="Message" name="message" value={mqtt.message} onChange={inputChanged}/>
            <button onClick={sendMqtt}>Send</button>

            <table>
                <thead>
                    <tr>
                        <th id="mqtt_topic">Topic</th>
                        <th id="mqtt_message">Message</th>
                    </tr>
                </thead>
                <tbody>{
                    topics.map((topic, index) => 
                    <tr key={index}>
                        <td>{topic.topic}</td>
                        <td>{topic.message}</td>
                    </tr>
                    )
                }</tbody>
            </table>
        </div>
      );
}

export default Mqtt