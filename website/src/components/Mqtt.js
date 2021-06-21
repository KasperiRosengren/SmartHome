import React, { useEffect, useState } from 'react';

function Mqtt(){
    const [mqtt, setmqtt] = useState({topic: 'test', message: 'test'});
    const [topics, setTopics] = useState([])
    const [topic, setTopic] = useState('');

    const inputChanged = (event) => {
        setmqtt({...mqtt, [event.target.name]: event.target.value});
    }

    const subscribeTopicChanged = (event) => {setTopic(event.target.value);}

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
        }).then(response => response.json())
        .then(data => {
          if(data.result === "failure"){
            alert(data.reason);
          }
      })
    }

    function subscribeTopic(){
      fetch('/api/mqtt/subscribe/topic', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        topic: topic
      })
    }).then(response => response.json())
    .then(data => {
      if(data.result === "failure"){
        alert(data.reason);
      }
      else{
        setTopics(data);
      }
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


    useEffect(() => {
      fetch('/api/mqtt/get/message/all')
      .then(response => response.json())
      .then(data => setTopics(data))
    }, []);

    return (
        <div className="MqttPageMain">
            <input placeholder="Topic" name="topic" value={mqtt.topic} onChange={inputChanged} />
            <input placeholder="Message" name="message" value={mqtt.message} onChange={inputChanged}/>
            <button onClick={sendMqtt}>Send</button>
            <br></br>
            <input placeholder="Topic" name="topic" value={topic} onChange={subscribeTopicChanged}/>
            <button onClick={subscribeTopic}>Subscribe</button>

            <table className="MqttTable">
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