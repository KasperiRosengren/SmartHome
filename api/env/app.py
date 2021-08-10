import time
import eventlet
from flask import Flask, request, jsonify, session
from flask_mqtt import Mqtt
from flask_mysqldb import MySQL
from urllib.parse import unquote_plus
from urllib.parse import unquote
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask_cors import CORS

app = Flask(__name__)

#configuration
eventlet.monkey_patch()
app.config.from_object('config.TestConfig')
#CORS(app, cors_allowed_origins='*')
mqtt = Mqtt(app)
mysql = MySQL(app)
socketio = SocketIO(app, debug=True, host="0.0.0.0", port=5000, cors_allowed_origins='*')
print('Starting up')
datatypelist = []
#region TestData

disIsGreatData = [{
      'zone': "Kitchen",    
      'temperature': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['20', '24', '27', '36']
              }, 
      'humidity': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['22', '27', '30', '40']
              },
               
      'outlets':
                [
                  {'name': "Coffee", 'value':"on"},
                  {'name': "Microwave", 'value':"off"},
                  {'name': "Oven", 'value':"off"},
                  {'name': "Blender", 'value':"off"},
                  {'name': "Boiler", 'value':"off"}
                ],
      'lights':
                [
                  {'name': "ceiling", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"blue", 'patterns': ['pattern1', 'pattern2', 'pattern1','pattern1','pattern1','pattern1','pattern1',]},
                  {'name': "Sink", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern3', 'pattern2']},
                  {'name': "Over Oven", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern1', 'pattern5']},
                  {'name': "Over Workbench", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"red", 'patterns': ['pattern100', 'pattern2']},
                  {'name': "Table", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"green", 'patterns': ['pattern12', 'pattern22']}
                ]
  }, {
      'zone': "BedRoom",    
      'temperature': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['20', '24', '27', '36']
              }, 
      'humidity': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['22', '27', '30', '40']
              },
               
      'outlets':
                [
                  {'name': "test", 'value':"on"},
                  {'name': "test1", 'value':"off"},
                  {'name': "test2", 'value':"on"},
                  {'name': "test3", 'value':"off"},
                  {'name': "test4", 'value':"on"}
                ],
      'lights':
                [
                  {'name': "ceiling", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"blue", 'patterns': ['pattern1', 'pattern2']},
                  {'name': "LeftWall", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern3', 'pattern2']},
                  {'name': "RightWall", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern1', 'pattern5']},
                  {'name': "Couch", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"red", 'patterns': ['pattern100', 'pattern2']},
                  {'name': "Workbench", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"green", 'patterns': ['pattern12', 'pattern22']}
                ]
  }, {
      'zone': "Hall",    
      'temperature': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['20', '24', '27', '36']
              }, 
      'humidity': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['22', '27', '30', '40']
              },
               
      'outlets':
                [
                  {'name': "test", 'value':"on"},
                  {'name': "test1", 'value':"off"},
                  {'name': "test2", 'value':"on"},
                  {'name': "test3", 'value':"off"},
                  {'name': "test4", 'value':"on"}
                ],
      'lights':
                [
                  {'name': "ceiling", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"blue", 'patterns': ['pattern1', 'pattern2']},
                  {'name': "LeftWall", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern3', 'pattern2']},
                  {'name': "RightWall", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern1', 'pattern5']}
                ]
  }, {
      'zone': "LivingRoom",    
      'temperature': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['20', '24', '27', '36']
              }, 
      'humidity': 
              {
                  'timestamp': ['05:00', '05:15', '05:30', '05:45'],
                  'values': ['22', '27', '30', '40']
              },
               
      'outlets':
                [
                  {'name': "test", 'value':"on"},
                  {'name': "test1", 'value':"off"},
                  {'name': "test2", 'value':"on"},
                  {'name': "test3", 'value':"off"},
                  {'name': "test4", 'value':"on"}
                ],
      'lights':
                [
                  {'name': "ceiling", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"blue", 'patterns': ['pattern1', 'pattern2']},
                  {'name': "LeftWall", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern3', 'pattern2']},
                  {'name': "RightWall", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"off", 'patterns': ['pattern1', 'pattern5']},
                  {'name': "Couch", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"red", 'patterns': ['pattern100', 'pattern2']},
                  {'name': "Workbench", 'statusValue':'off', 'statusPattern':'pattern1', 'value':"green", 'patterns': ['pattern12', 'pattern22']}
                ]
  }]

#endregion

#region TestAPI
@app.route('/api/test/test', methods = ['POST', 'GET'])
def api_test_test():
    return jsonify(disIsGreatData)


@app.route('/api/new/test', methods = ['POST'])
def api_new_test():
    outlet_command = request.get_json()
    zone = outlet_command.get('zone')
    outletName = outlet_command.get('name')
    command = outlet_command.get('command')

    for data in disIsGreatData:
        if zone == data['zone']:
            for outlet in data['outlets']:
                if outletName == outlet['name']:
                    outlet['value'] = command
                    topic = (f'building/{zone}/device/{outletName}')
                    mqtt.publish(topic, command)
                    print(topic)
                    print(command)
                    return {"result": "success"}
    return {"result": "failure"}


@app.route('/api/new/test1', methods = ['POST'])
def api_new_test1():
    light_command = request.get_json()
    zone = light_command.get('zone')
    lightName = light_command.get('name')
    color = light_command.get('color')

    for data in disIsGreatData:
        if zone == data['zone']:
            for light in data['lights']:
                if lightName == light['name']:
                    light['statusValue'] = color
                    topic = (f'building/{zone}/device/{lightName}')
                    mqtt.publish(topic, color)
                    print(topic)
                    print(color)
                    return {"result": "success"}
    return {"result": "failure"}



@app.route('/api/new/test2', methods = ['POST'])
def api_new_test2():
    light_command = request.get_json()
    zone = light_command.get('zone')
    lightName = light_command.get('name')
    pattern = light_command.get('pattern')

    for data in disIsGreatData:
        if zone == data['zone']:
            for light in data['lights']:
                if lightName == light['name']:
                    light['statusPattern'] = pattern
                    topic = (f'building/{zone}/device/{lightName}')
                    mqtt.publish(topic, pattern)
                    print(topic)
                    print(pattern)
                    return {"result": "success"}
    return {"result": "failure"}


@app.route('/api/get/frontend/init', methods = ['GET'])
def api_get_frontend_init():
    #Check if user is logged in
    #If not, return result failure
    #Otherwise continue on
    if session.get('userID'):
        userID = session.get('userID')
        cursor = mysql.connection.cursor()
        cursor.execute(f"CALL frontend_init({userID})")
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()
        
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        cursor.close()
        print(json_data)
        return jsonify(json_data)
    
    else:
        return {"result": "failure"}



@app.route('/api/get/frontend/test/init', methods = ['GET'])
def api_get_frontend_test_init():
    #Check if user is logged in
    #If not, return result failure
    #Otherwise continue on
    cursor = mysql.connection.cursor()
    cursor.execute(f'CALL new_frontend_init("SuperAdmin")')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    print(json_data)
    return jsonify(json_data)
    



#endregion





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




#region MQTT


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('MQTT connected')
    mqtt.subscribe('goodtopic')
    mqtt.subscribe('test')

def init_mqtt_topics_mysql():

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT Building, Zone, Device FROM mqtt_topics")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
    
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    mydevices = []
    for data in json_data:
        topicbeginning = f"{data['Building']}/{data['Zone']}/{data['Device']}"
        mydevices.append(topicbeginning)

    cursor = mysql.connection.cursor()
    cursor.execute(f"DESCRIBE devices")
    mydatatypes = cursor.fetchall()
    cursor.close()
    
    dataList = []
    for datatype in mydatatypes:
        dataList.append(datatype)
    del dataList[0:5]
    datatypes = []
    for datatype in dataList:
        topicend = datatype[0]
        datatypelist.append(topicend)
        datatypes.append(topicend)

    topiclist = []
    for device in mydevices:
        for datatype in datatypes:
            thistopic = (f'{device}/{datatype}')
            topiclist.append(thistopic)
            
    
    for topic in topiclist:
        print(topic)
        mqtt.subscribe(topic)

    print('All topics subscribed to!')




@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    #print(data)
    #
    topicSplitted = data['topic'].split('/')
    Building = topicSplitted[0]
    Zone = topicSplitted[1]
    Device = topicSplitted[2]
    DataType = topicSplitted[3]
    #print(f'Building: {topicSplitted[0]}, Zone: {topicSplitted[1]}, Device: {topicSplitted[2]}, DataType: {topicSplitted[3]}')
    print(f'Building: {Building}, Zone: {Zone}, Device: {Device}, DataType: {DataType}')
    print(f'Topic: {data["topic"]}, with data: {data["payload"]}')
    #socketio.emit('roomData', {'tst': '06:00', 'temp': '17', 'hum': '22'}, namespace=(f'/{data["topic"]}'))
    #for thistopic in mqtt_messages:
        #if thistopic['topic'] == data['topic']:
            #socketio.emit('roomData', {'tst': '06:00', 'temp': '17', 'hum': '22'}, room=data['topic'])
            
            #thistopic['message'] = data['payload']
            #return

    if DataType in datatypelist:
        if DataType == 'lights' or DataType == 'outlets' or DataType == 'doorlock':
            #This shouldn't even happen!?!?!
            pass
        elif DataType == "keybad":
            print("adding data to keybad")
            cursor = mysql.connection.cursor()
            cursor.execute(f'CALL add_data_keybad({Building},{Zone},{Device},{data["payload"]})')
            myresult = cursor.fetchone()
            cursor.close()
            #Send the data to MySQL
        else:
            print(f'Add some {DataType} data')
            #Send the new data to MySQL
            cursor = mysql.connection.cursor()
            cursor.execute(f'CALL add_data_{DataType}("{Building}","{Zone}","{Device}","{data["payload"]}")')
            myresult = cursor.fetchone()
            cursor.close()

            #Send the data to socketio
            socketio.emit('newData', {'tst': '06:00', 'temp': '17', 'hum': '22'}, namespace=(f'/{Building}/{Zone}'), room=DataType)




#endregion




#region SocketIO


@socketio.on('message')
def handle_message(data):
    socketio.emit('some event', {'data': 42})
    print('received message: ' + data)


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)
    print(f'{username} has joined room: {room}')

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)
    print(f'{username} has left room: {room}')

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('tester', namespace='/building/Kitchen')
def building_kitchen_tester(data):
    print(f'Kitchen: {data}')

@socketio.on('tester', namespace='/building/BedRoom')
def building_bedroom_tester(data):
    print(f'BedRoom: {data}')

@socketio.on('tester', namespace='/building/Hall')
def building_hall_tester(data):
    print(f'Hall: {data}')

@socketio.on('tester', namespace='/building/LivingRoom')
def building_livingroom_tester(data):
    print(f'LivingRoom: {data}')


#endregion





#region API

#region MQTT
@app.route('/api/mqtt/get/message/all')
def mqtt_get_message_all():
    return jsonify(mqtt_messages)

@app.route('/api/mqtt/send/message', methods = ['POST'])
def mqtt_send_message():
    mqtt_json = request.get_json()
    topic = mqtt_json.get('topic')
    message = mqtt_json.get('message')

    for thistopic in mqtt_messages:
        if thistopic['topic'] == topic:
            mqtt.publish(topic, message)
            return {'result': 'success'}
    
    return {'result': 'failure', 'reason': 'Topic does not exist'}

@app.route('/api/mqtt/subscribe/topic', methods = ['POST'])
def mqtt_subscribe_topic():
    mqtt_json = request.get_json()
    topic = mqtt_json.get('topic')
    for thistopic in mqtt_messages:
        if thistopic['topic'] == topic:
            return {'result': 'failure', 'reason': 'Topic already subscribed to'}
        
    mqtt_messages.append({'topic': topic, 'message': 'subscibed'})
    mqtt.subscribe(topic)
    return jsonify(mqtt_messages)
#endregion  

#region Control

#region Devices
#region Outlets

#Controll specific outlets status
@app.route('/api/control/device/outlet/status', methods = ['POST'])
def api_control_device_outlet_status():
    outlet_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    outletName = outlet_command.get('name')
    command = outlet_command.get('command')
    #Check if user is logged in
    if session.get('userID'):
        #User is logged in, and found the userID

        #Check if user has permission to control this device
        #Get user access to zone's devices
        userID = session.get('userID')
        cursor = mysql.connection.cursor()
        cursor.execute(f'CALL get_user_access_zone_status({userID},"{building}","{zone}")')
        #results = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()
    
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        cursor.close()
        userAccess = []
        for data in json_data:
            userAccess.append(data['StatusAccess'])
        #userAccess = []
        #for access in results:
            #userAccess.append(access)
        
        #cursor.close()

        print(userAccess)
        allowedAccess = ['F', 'E', 'D', 'C', '7', '6', '5', '4']
        #Check if user has permission to control device

        if userAccess == 'Building does not exist':
            return {"result": "failure", "reason": "Building does not exist"}

        elif userAccess == 'This zone does not exist in this building':
            return {"result": "failure", "reason": "This zone does not exist in this building"}

        for allow in allowedAccess:
            for user in userAccess:
                print(f'Compare {allow} to {user}')
                if allow == user:
                    #User has permission to control device
                    #Send command to
                    print('Access granted')
                    return {"result": "success"}
                    
        
        #User did not have permission
        return {"result": "failure", "reason": "user does not have permission for this zone"}
        #IF permission == true
            #Send command to mqtt
            #Send command to MySQL
            #Send command to SocketIO
            #Return result success
        
        #Elif   Permission == False
            #Return no access to this device

        #Elif   building/zone/device not found
            #Specify which wasn't found and return that as error not found
        
        #Else
            #Result server error
    else:
        return {"result": "failure", "reason": "not logged in"}

    
    return {"result": "failure"}


#endregion Outlets

#region Lights

@app.route('/api/control/device/light/status', methods = ['POST'])
def api_control_device_light_status():
    light_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    lightName = outlet_command.get('name')
    status = outlet_command.get('status')

    #Check if user has permission to control this device
    #IF permission == true
        #Send command to mqtt
        #Send command to MySQL
        #Send command to SocketIO
        #Return result success
    
    #Elif   Permission == False
        #Return no access to this device

    #Elif   building/zone/device not found
        #Specify which wasn't found and return that as error not found
    
    #Else
        #Result server error

    
    return {"result": "failure"}





@app.route('/api/control/device/light/pattern', methods = ['POST'])
def api_control_device_light_pattern():
    light_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    lightName = outlet_command.get('name')
    pattern = outlet_command.get('pattern')

    #Check if user has permission to control this device
    #IF permission == true
        #Send command to mqtt
        #Send command to MySQL
        #Send command to SocketIO
        #Return result success
    
    #Elif   Permission == False
        #Return no access to this device

    #Elif   building/zone/device not found
        #Specify which wasn't found and return that as error not found
    
    #Else
        #Result server error

    
    return {"result": "failure"}

@app.route('/api/control/device/light/speed', methods = ['POST'])
def api_control_device_light_speed():
    light_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    lightName = outlet_command.get('name')
    speed = outlet_command.get('speed')

    #Check if user has permission to control this device
    #IF permission == true
        #Send command to mqtt
        #Send command to MySQL
        #Send command to SocketIO
        #Return result success
    
    #Elif   Permission == False
        #Return no access to this device

    #Elif   building/zone/device not found
        #Specify which wasn't found and return that as error not found
    
    #Else
        #Result server error

    
    return {"result": "failure"}

@app.route('/api/control/device/light/color', methods = ['POST'])
def api_control_device_light_color():
    light_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    lightName = outlet_command.get('name')
    color = outlet_command.get('color')

    #Check if user has permission to control this device
    #IF permission == true
        #Send command to mqtt
        #Send command to MySQL
        #Send command to SocketIO
        #Return result success
    
    #Elif   Permission == False
        #Return no access to this device

    #Elif   building/zone/device not found
        #Specify which wasn't found and return that as error not found
    
    #Else
        #Result server error

    
    return {"result": "failure"}




#endregion Lights


#endregion Devices
#endregion Control



#region Alter
#region Oultets
#Controll specific outlet's name
@app.route('/api/alter/device/outlet/name', methods = ['POST'])
def api_alter_device_outlet_name():
    outlet_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    outletName = outlet_command.get('name')
    newName = outlet_command.get('newname')

    #Check if user has permission to control this device
    #IF permission == true
        #Send command to mqtt
        #Send command to MySQL
        #Send command to SocketIO
        #Return result success
    
    #Elif   Permission == False
        #Return no access to this device

    #Elif   building/zone/device not found
        #Specify which wasn't found and return that as error not found
    
    #Else
        #Result server error

    
    return {"result": "failure"}


#endregion Outlets

#endregion Alter
#region MySQL

@app.route('/mysql', methods = ['POST'])
def mysql_post():
    mysql_json = request.get_json()
    table = mysql_json.get('table')
    jokuNimi = mysql_json.get('jokuNimi')

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO testi (jokuNimi) VALUES('{jokuNimi}')")
    mysql.connection.commit()
    cursor.close()
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


@app.route('/api/mysql/user/data', methods = ['POST', 'GET'])
def api_mysq_user_data():
    #Get all zones and their data that belongs to the logged user
    if session.get('userName'):
        return jsonify(disIsGreatData)
    else:
        return {"result": "failure", "reason": "not logged in"}
#endregion


#region Authentication
@app.route('/api/auth/login', methods = ['POST'])
def auth_login():
    init_mqtt_topics_mysql()
    mysql_json = request.get_json()
    username = mysql_json.get('username')
    password = mysql_json.get('password')           
    print(username)
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

def get_user_mqtt_topics():
    if session.get('userID'):
        cursor = mysql.connection.cursor()
        cursor.callproc('get_user_mqtt_topics',[session['userID']])
        myresult = cursor.fetchall()

        if myresult != None:
            mqtt_topics = []
            for row in myresult:
                building = row[0]
                zone = row[1]
                device = row[2]
                i = 0
                for dtype in row:
                    data_type = dtype[i]
                    topic = (f'{building}/{zone}/{device}/{data_type}')
                    mqtt_topics.append(topic)
                    i += 1

            session['topics'] = mqtt_topics

        cursor.close()


@app.route('/api/auth/logout', methods = ['GET'])
def auth_logout():
    if session.get('userName'):
        session.pop('userName', default=None)
    if session.get('userID'):
        session.pop('userID', default=None)
    return {'result': 'success'}

@app.route('/api/auth/whoami', methods = ['GET'])
def auth_whoami():
    init_mqtt_topics_mysql()
    if session.get('userID'):
        return {'name': session['userName'], 'id': session['userID']}
    return {'name': "You are not logged in", 'id': "You are not logged in"}
#endregion

#endregion


print('All run')

if __name__ == '__main__':
    #socketio.run(app)
    socketio.run(app, host="0.0.0.0", port=5000)
    #app.run(debug=True)