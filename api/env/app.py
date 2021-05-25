import time
from flask import Flask, request, jsonify, session
from flask_mqtt import Mqtt
from flask_mysqldb import MySQL
from urllib.parse import unquote_plus
from urllib.parse import unquote

app = Flask(__name__)

#configuration

app.config.from_object('config.TestConfig')
mqtt = Mqtt(app)
mysql = MySQL(app)

mqtt_messages = [{
    'topic': 'testtopic',
    'message': 'testmessage'},
{
    'topic': 'anothertopic',
    'message': 'nicemessage'}
]

###Test if api connection works. Return the current time
@app.route('/time')
def get_current_time():
    return {'time': time.localtime()}

### Start of mqtt settings
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('goodtopic')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)
    if not any(d.get('main_color', default_value) == 'red' for d in a):
        # does not exist
        mqtt_messages.append({'topic': data.topic, 'message': data.payload})
    

### Start of mqtt api
@app.route('/api/mqtt/get/message/all')
def mqtt_get_message_all():
    print(jsonify(mqtt_messages))
    return jsonify(mqtt_messages)

@app.route('/api/mqtt/send/message', methods = ['POST'])
def mqtt_send_message():
    mqtt_json = request.get_json()
    topic = mqtt_json.get('topic')
    message = mqtt_json.get('message')
    mqtt.publish(topic, message)
    return {'topic': topic, 'message': message}
    
### Start of MySQL api
@app.route('/mysql', methods = ['POST'])
def mysql_post():
    mysql_json = request.get_json()
    table = mysql_json.get('table')
    jokuNimi = mysql_json.get('jokuNimi')

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO testi (jokuNimi) VALUES('{jokuNimi}')")
    mysql.connection.commit()
    return 'message sent'


@app.route('/mysql/select', methods = ['POST'])
def mysql_select():
    mysql_json = request.get_json()
    table = mysql_json.get('table')
    jokuNimi = mysql_json.get('jokuNimi')

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
    
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    return jsonify(json_data)


@app.route('/api/mysql/user/devices')
def mysql_user_devices():
    if session.get('userID'):
        userID = session.get('userID')
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM users")
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()
        
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        cursor.close()
        return jsonify(json_data)
    
    else:
        return {"result": "failure"}



### Start of Authentication API
@app.route('/api/auth/login', methods = ['POST'])
def auth_login():
    mysql_json = request.get_json()
    username = mysql_json.get('username')
    password = mysql_json.get('password')           
    
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    cursor.execute(f'SELECT idusers, username FROM users WHERE username="{username}" AND password="{password}"')
    myresult = cursor.fetchone()
    cursor.close()
    if myresult != None:
        print(f"UserID: {myresult[0]}")
        session['userID'] = myresult[0]
        session['userName'] = myresult[1]
        return {"result": "success"}
    return {"result": "failure"}


@app.route('/api/auth/logout', methods = ['GET'])
def auth_logout():
    if session.get('userName'):
        session.pop('userName', default=None)
    if session.get('userID'):
        session.pop('userID', default=None)
    return {'result': 'success'}

@app.route('/api/auth/whoami', methods = ['GET'])
def auth_whoami():
    if session.get('userID'):
        return {'name': session['userName'], 'id': session['userID']}
    return {'name': "You are not logged in", 'id': "You are not logged in"}
