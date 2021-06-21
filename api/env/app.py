import time
from flask import Flask, request, jsonify, session
from flask_mqtt import Mqtt
from flask_mysqldb import MySQL
from urllib.parse import unquote_plus
from urllib.parse import unquote
from flask_socketio import SocketIO

app = Flask(__name__)

# Maybe I need to add every session into a list? or maybe a dictionary?
# sessions.append(session)      or something like that
#  with dict I could store every topic for specific user
#

# Or maybe I need to create a dictionary for topics
# And someway add the sessions into every topic
# they have access to
# example = [{'UserID': 1, 'topics': ['building/zone/device/datatype', 'building/zone/device/datatype']},
#           {'UserID': 2, 'topics': ['building/zone/device/datatype', 'building/zone/device/datatype']}]

# Maybe I just store the topics on Front end and when I get new mqtt message
# I send the topic to every session and then the frontend answers if
# that is it's topic or not
# if it is, then the message + gets sent to the front end and it can store the message on there

# Or maybe send all topics for the specific user to frontend
# and then React-mqtt can subscribe to those topics

# Try subscribing to same topic twice
# build/zone/dev/temp
# AND
# build/zone/#
# OR
# build/zone/+/temp
#
# Depending on what the user needs

# Create a room for each zone
# Add sockets to rooms based on access level

# I need API path for sending button values from react to mqtt


#configuration
app.config.from_object('config.TestConfig')
mqtt = Mqtt(app)
mysql = MySQL(app)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)
#
#
#
#
#
#
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
                  'values': ['20', '24', '27', '36']
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
                  'values': ['20', '24', '27', '36']
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
                  'values': ['20', '24', '27', '36']
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
                  'values': ['20', '24', '27', '36']
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

#
#
#
#
#
#











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
    mqtt.subscribe('test')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)
    for thistopic in mqtt_messages:
        if thistopic['topic'] == data['topic']:
            thistopic['message'] = data['payload']
            return

    mqtt_messages.append({'topic': data['topic'], 'message': data['payload']})

################################
########        API     ########
################################

########       MQTT     ########
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
    


########       MySQL     ########
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



########       AUTH     ########
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
    if session.get('userID'):
        return {'name': session['userName'], 'id': session['userID']}
    return {'name': "You are not logged in", 'id': "You are not logged in"}
