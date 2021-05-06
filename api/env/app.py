import time
from flask import Flask, request, jsonify
from flask_mqtt import Mqtt

app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = '192.168.1.205'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

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
