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

#endregion


@app.route('/api/get/frontend/init', methods = ['GET'])
def api_get_frontend_init():
    #Check if user is logged in
    #If not, return result failure
    #Otherwise continue on
    if session.get('userName'):
        userName = session.get('userName')
        print(F"User: {userName}")
        cursor = mysql.connection.cursor()
        cursor.execute(f"CALL new_frontend_init('{userName}')")
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
    cursor.close()
    mysql.connection.commit()
    
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    
    print(json_data)
    return jsonify(json_data)




@app.route('/api/get/zone/temperature/daily', methods = ['POST'])
def api_get_zone_temperature_daily():

    get_command = request.get_json()
    building = get_command.get('building')
    zone = get_command.get('zone')

    cursor = mysql.connection.cursor()
    cursor.execute(f'CALL get_zone_temperature_daily("{building}", "{zone}")')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    print(json_data)
    return jsonify(json_data)
    



#endregion


###Test if api connection works. Return the current time
@app.route('/time')
def get_current_time():
    return {'time': time.localtime()}




#region MQTT


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('MQTT connected')


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
    #socketio.emit('roomData', {'tst': '06:00', 'temp': '17', 'hum': '22'}, room=data['topic'])

    if DataType == 'lights' or DataType == 'outlets' or DataType == 'doorlock':
        print(f"message from {DataType}")
        #This shouldn't even happen!?!?!
        pass
    elif DataType == "keybad":
        print("Keybad data")
        #Send the data to MySQL
    else:
        print(f'Add some {DataType} data')
        socketio.emit('newData', data["payload"], namespace=(f'{DataType}'), to=(f"{Building}_{Zone}_{Device}"))
        #Send the data to socketio
        #socketio.emit('newData', {'tst': '06:00', 'temp': '17', 'hum': '22'}, namespace=(f'/{Building}/{Zone}'), room=DataType)




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



#SubscribedTopics = {
#   "home/Kitchen/Weatherstation/temperature": 
#   {
#       "GreatUsername": [instance, instance, instance],
#       "AnotherGreatUsername": [instance]
#   },
#   "home/Kitchen/Weatherstation/humidity":
#   {
#       "GreatUsername": [instance, instance, instance],
#       "AnotherGreatUsername": [instance]
#   }
# }
SubscribedTopics = {}


@socketio.on('join', namespace='/temperature')
def on_join_temperature(data):
    room = data['room']
    join_room(room)
    topic = f'{data["building"]}/{data["zone"]}/{data["device"]}/temperature'

    #Check if topic has already been subscribed to
    if topic in SubscribedTopics:
        #If has, get user name from flask session
        if session.get('userName'):
            thisusername = session.get('userName')
            #Check if user already has subscribed to topic
            #if has, append the lis, if not, create list and add first
            if thisusername in SubscribedTopics[topic]:
                SubscribedTopics[topic][thisusername].append("instance")
            else:
                SubscribedTopics[topic][thisusername] = ["instance"]
    else:
        mqtt.subscribe(topic)
        SubscribedTopics[topic] = {}
    print(f'Someone joined room: {room}')

@socketio.on('leave', namespace='/temperature')
def on_leave_temperature(data):
    room = data['room']
    leave_room(room)
    mqtt.unsubscribe(f'{data["building"]}/{data["zone"]}/{data["device"]}/temperature')
    print(f'Someone left room: {room}')



#endregion





#region API

#region Control

#region Devices
#region Outlets

#Controll specific outlets status
@app.route('/api/control/device/outlet/status', methods = ['POST'])
def api_control_device_outlet_status():
    outlet_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    boxName = outlet_command.get('box')
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
                    #Send command to outlet and responseback to original sender
                    topic = f'controll/{building}/{zone}/outlets/{boxName}/{outletName}'
                    mqtt.publish(topic, command)
                    print(f'Topic: {topic}, Payload: {command}')
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

@app.route('/api/control/device/light', methods = ['POST'])
def api_control_device_light():
    light_command = request.get_json()
    building = outlet_command.get('building')
    zone = outlet_command.get('zone')
    lightName = outlet_command.get('name')
    status = outlet_command.get('status')
    pattern = outlet_command.get('pattern')
    speed = outlet_command.get('speed')
    color_0 = outlet_command.get('color_0')
    color_1 = outlet_command.get('color_1')
    color_2 = outlet_command.get('color_2')

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




@app.route('/api/control/device/light/status', methods = ['POST'])
def api_control_device_light_status():
    light_command = request.get_json()
    building = light_command.get('building')
    zone = light_command.get('zone')
    lightName = light_command.get('name')
    status = light_command.get('status')

    if(status == "on"):
        status = "off"
    else:
        status = "on"

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

    topic = f'controll/{building}/{zone}/lights/{lightName}/status'
    mqtt.publish(topic, status)
    print(f'Topic: {topic}, Payload: {status}')

    return {"result": "success"}
    #return {"result": "failure"}





@app.route('/api/control/device/light/pattern', methods = ['POST'])
def api_control_device_light_pattern():
    light_command = request.get_json()
    building = light_command.get('building')
    zone = light_command.get('zone')
    lightName = light_command.get('name')
    pattern = light_command.get('pattern')
    
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

    topic = f'controll/{building}/{zone}/lights/{lightName}/pattern'
    mqtt.publish(topic, pattern)
    print(f'Topic: {topic}, Payload: {pattern}')

    return {"result": "success"}
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
    building = light_command.get('building')
    zone = light_command.get('zone')
    lightName = light_command.get('name')
    color = light_command.get('color')
    newColor = light_command.get('newColor')

    topic = f'controll/{building}/{zone}/lights/{lightName}/{color}'
    mqtt.publish(topic, newColor)
    print(f'Topic: {topic}, Payload: {newColor}')
    
    return({"result": "success"})

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
#This is for altering device names, locations etc.

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



#region Controlpanel

    #region GetData
#Get all buildings
@app.route('/api/get/controlpanel/buildings', methods = ['GET'])
def api_get_controlpanel_buildings():
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    cursor.execute(f'SELECT name, address, idbuilding AS id from building')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    return jsonify(json_data)



#Get all zones
@app.route('/api/get/controlpanel/zones', methods = ['GET'])
def api_get_controlpanel_zones():
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    cursor.execute(f'SELECT b.name AS buildingname, z.name AS zonename, idzone AS id from zone z JOIN building b ON z.idbuilding=b.idbuilding')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    return jsonify(json_data)




#Get all devices
@app.route('/api/get/controlpanel/devices', methods = ['GET'])
def api_get_controlpanel_devices():
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    cursor.execute(f'SELECT b.name AS buildingname, z.name AS zonename, d.name AS devicename, iddevices AS id from devices d JOIN zone z ON d.idzone=z.idzone JOIN building b ON z.idbuilding=b.idbuilding')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    return jsonify(json_data)



#Get all roles
@app.route('/api/get/controlpanel/roles', methods = ['GET'])
def api_get_controlpanel_roles():
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    cursor.execute(f'SELECT name, idroles AS id FROM roles ORDER BY id')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    return jsonify(json_data)



#Get all users
@app.route('/api/get/controlpanel/users', methods = ['GET'])
def api_get_controlpanel_users():
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    cursor.execute(f'SELECT username, idusers AS id FROM users ORDER BY id')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
        
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    return jsonify(json_data)

    #endregion


    #region CreateNew

#Create new building
@app.route('/api/controlpanel/create/building', methods = ['POST'])
def api_controlpanel_create_building():
    mysql_json = request.get_json()
    name = mysql_json.get('name')
    address = mysql_json.get('address')           
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    print(f"Given name: {name}, and address: {address}")
    cursor.execute(f'CALL add_new_building("{name}", "{address}")')
    myresult = cursor.fetchone()
    cursor.close()
    mysql.connection.commit()
    if myresult != None:
        if myresult[0] != "Building already exists":
            print(f"BuildingID: {myresult[0]}")
            return {"result": "success"}
        else:
            print(myresult[0])
            return {"result": "failure", "reason": "Building already exists"}
    else:
        print("Something went wrong!")
        return {"result": "failure", "reason": "unknown"}




#Create new zone
@app.route('/api/controlpanel/create/zone', methods = ['POST'])
def api_controlpanel_create_zone():
    mysql_json = request.get_json()
    building = mysql_json.get('building')
    zone = mysql_json.get('zone')           
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    print(f"Given ZoneName: {zone}, and building: {building}")
    cursor.execute(f'CALL add_new_zone("{zone}", "{building}")')
    myresult = cursor.fetchone()
    cursor.close()
    mysql.connection.commit()
    if myresult != None:
        if myresult[0] == "Zone already exists":
            print("Zone already exists")
            return {"result": "failure", "reason": "Zone already exists"}

        elif myresult[0] == "Building does not exist":
            print("Building does not exist")
            return {"result": "failure", "reason": "Building does not exist"}
        else:
            print(f"ZoneID: {myresult[0]}")
            return {"result": "success"}
    else:
        print("Something went wrong!")
        return {"result": "failure", "reason": "unknown"}




#Create new Device
@app.route('/api/controlpanel/create/device', methods = ['POST'])
def api_controlpanel_create_device():
    mysql_json = request.get_json()
    building = mysql_json.get('building')
    zone = mysql_json.get('zone')
    device = mysql_json.get('device')  
    location = mysql_json.get('location')          
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    print(f"Data given: Building: {building}, Zone: {zone}, Device{device} and location: {location}")
    cursor.execute(f'CALL add_new_device("{building}", "{zone}", "{device}", "{location}")')
    myresult = cursor.fetchone()
    cursor.close()
    mysql.connection.commit()
    if myresult != None:
        if myresult[0] == "Zone does not exist":
            print("Zone already exists")
            return {"result": "failure", "reason": "Zone already exists"}

        elif myresult[0] == "Building does not exist":
            print("Building does not exist")
            return {"result": "failure", "reason": "Building does not exist"}

        elif myresult[0] == "Device already exists":
            print("Device already exists")
            return {"result": "failure", "reason": "Device already exists"}

        else:
            print(f"DeviceID: {myresult[0]}")
            return {"result": "success"}
    else:
        print("Something went wrong!")
        return {"result": "failure", "reason": "unknown"}





#Create new role
@app.route('/api/controlpanel/create/role', methods = ['POST'])
def api_controlpanel_create_role():
    mysql_json = request.get_json()
    name = mysql_json.get('name')          
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    print(f"Given Role name: {name}")
    cursor.execute(f'CALL add_new_role("{name}")')
    myresult = cursor.fetchone()
    cursor.close()
    mysql.connection.commit()
    if myresult != None:
        if myresult[0] != "Role already exists":
            print(f"RoleID: {myresult[0]}")
            return {"result": "success"}
        else:
            print(myresult[0])
            return {"result": "failure", "reason": "Role already exists"}
    else:
        print("Something went wrong!")
        return {"result": "failure", "reason": "unknown"}




#Create new user
@app.route('/api/controlpanel/create/user', methods = ['POST'])
def api_controlpanel_create_user():
    mysql_json = request.get_json()
    name = mysql_json.get('name')
    password = mysql_json.get('password')
    cursor = mysql.connection.cursor()
    #Fetch the user id for the given name and password
    print(f"Given Username: {name}")
    cursor.execute(f'CALL add_new_user("{name}", "{password}")')
    myresult = cursor.fetchone()
    cursor.close()
    mysql.connection.commit()
    if myresult != None:
        if myresult[0] != "User already exists":
            print(f"UserID: {myresult[0]}")
            return {"result": "success"}
        else:
            print(myresult[0])
            return {"result": "failure", "reason": "User already exists"}
    else:
        print("Something went wrong!")
        return {"result": "failure", "reason": "unknown"}






    #endregion


#endregion

#region Authentication
@app.route('/api/auth/login', methods = ['POST'])
def auth_login():
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
#endregion
#endregion


print('All run')

if __name__ == '__main__':
    #socketio.run(app)
    socketio.run(app, host="0.0.0.0", port=5000)
    #app.run(debug=True)