import React, { useState } from 'react';

function Devices(){
    const [mysql, setMysql] = useState({table: '', jokuNimi: ''});
    const [users, setUsers] = useState([])

    const insertChanged = (event) => {
        setMysql({...mysql, [event.target.name]: event.target.value});
      }

    function sendMysql(){
        fetch('/mysql', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            table: mysql.table,
            jokuNimi: mysql.jokuNimi
        })
      })
    }

    function getMysql(){
        fetch('/api/mysql/devices', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ table: mysql.table, jokuNimi: mysql.jokuNimi })
        })
        .then(response => response.json())
        .then(json => setUsers(json))
    }

    return (
        <div className="MysqlPageMain">
            <p>Insert into table</p>
            <input placeholder="Table" name="table" value={mysql.table} onChange={insertChanged} />
            <input placeholder="JokuNimi" name="jokuNimi" value={mysql.jokuNimi} onChange={insertChanged} />
            <button onClick={sendMysql}>Send</button>
            <button onClick={getMysql}>Get</button>
            <table className="MysqlTable">
                <thead>
                    <tr>
                        <th id="users_ID">ID</th>
                        <th id="users_jokuNimi">jokuNimi</th>
                    </tr>
                </thead>
                <tbody>{
                    users.map((user, index) => 
                    <tr key={index}>
                        <td>{user.id}</td>
                        <td>{user.jokuNimi}</td>
                    </tr>
                    )
                }</tbody>
            </table>
        </div>
      );
}

export default Devices