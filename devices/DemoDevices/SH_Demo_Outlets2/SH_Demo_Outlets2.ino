#include <WiFi.h>
#include <PubSubClient.h>


// Replace the next variables with your SSID/Password combination
const char* ssid = "SSID";
const char* password = "PASSWORD";

// Add your MQTT Broker IP address, example:
const char* mqtt_server = "192.168.0.106";
const int mqtt_port = 2883;


String building = "Garage";
String zone = "Inside";
String deviceName = "Outlets";

WiFiClient clientname;
PubSubClient client(clientname);
long lastMsg = 0;
char msg[50];
int value = 0;

//Pins for outlets in BOX 0
const int Garage_Box0_Out0 = 4;
const int Garage_Box0_Out1 = 13;

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
  setup_pins();
}

void setup_pins(){
  //Set pins for box 0
  pinMode(Garage_Box0_Out0, OUTPUT);
  pinMode(Garage_Box0_Out1, OUTPUT);

  //Set pins to low for box 0
  digitalWrite(Garage_Box0_Out0, LOW);
  digitalWrite(Garage_Box0_Out1, LOW);
}


void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
