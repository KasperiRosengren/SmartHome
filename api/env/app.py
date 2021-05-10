import time
from flask import Flask, request, jsonify
from flask_mqtt import Mqtt
from flask_mysqldb import MySQL

app = Flask(__name__)

#configuration

app.config.from_object('config.TestConfig')
mqtt = Mqtt(app)
mysql = MySQL(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('home/mytopic')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('home/mytopic')

@app.route('/time')
def get_current_time():
    return {'time': time.localtime()}

@app.route('/mqtt', methods = ['POST'])
def mqtt_send_message():
    mqtt_json = request.get_json()
    topic = mqtt_json.get('topic')
    message = mqtt_json.get('message')
    mqtt.publish(topic, message)
    return 'message sent'

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
    return jsonify(json_data)