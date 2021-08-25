import paho.mqtt.client as mqtt
import mysql.connector

mydb = mysql.connector.connect(
  host='',
  user="",
  password="",
  database=""
)

datatypelist = []

def init_mqtt_topics():
    
    cursor = mydb.cursor()
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

    cursor = mydb.cursor()
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
        client.subscribe(topic)

    print('All topics subscribed to!')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")

    topicSplitted = msg.topic.split('/')
    Building = topicSplitted[0]
    Zone = topicSplitted[1]
    Device = topicSplitted[2]
    DataType = topicSplitted[3]
    #print(f'Building: {topicSplitted[0]}, Zone: {topicSplitted[1]}, Device: {topicSplitted[2]}, DataType: {topicSplitted[3]}')
    print(f'Building: {Building}, Zone: {Zone}, Device: {Device}, DataType: {DataType}')
    print(f'Topic: {msg.topic}, with data: {payload}')

    if DataType in datatypelist:
        if DataType == 'lights' or DataType == 'outlets' or DataType == 'doorlock':
            #This shouldn't even happen!?!?!
            pass
        elif DataType == "keybad":
            print("adding data to keybad")
            cursor = mydb.cursor()
            cursor.execute(f'CALL add_data_keybad({Building},{Zone},{Device},{payload})', multi=True)
            myresult = cursor.fetchone()
            cursor.close()
            #Send the data to MySQL
        else:
            print(f'Add some {DataType} data')
            #Send the new data to MySQL
            #cursor = mydb.cursor()
            #query = f'CALL add_data_{DataType}("{Building}","{Zone}","{Device}","{payload}")'
            #print(f'Query: {query}')
            #cursor.execute(query, multi=True)
            #myresult = cursor.fetchone()
            #cursor.close()
            #print(myresult)

            cursor = mydb.cursor()
            #arguments = [f'{Building}', f'{Zone}', f'{Device}', f'{payload}']
            #query = f'add_data_{DataType}'
            cursor.callproc(f'add_data_{DataType}', [Building, Zone, Device, payload])

            mydb.commit()
            cursor.close()
            #print(f'Myresult: {myresult}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.171", 2883, 60)
init_mqtt_topics()
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()