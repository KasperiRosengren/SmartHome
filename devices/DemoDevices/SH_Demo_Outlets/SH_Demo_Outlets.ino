#include <WiFi.h>
#include <PubSubClient.h>


// Replace the next variables with your SSID/Password combination
const char* ssid = "SSID";
const char* password = "PASSWORD";

// Add your MQTT Broker IP address, example:
const char* mqtt_server = "192.168.0.106";
const int mqtt_port = 2883;


String building = "House";
String zone = "All";
String deviceName = "Outlets";

WiFiClient clientname;
PubSubClient client(clientname);
long lastMsg = 0;
char msg[50];
int value = 0;

//Pins for outlets in BOX 0
const int Kitchen_Box0_Out0 = 4;
const int Kitchen_Box0_Out1 = 13;
const int Kitchen_Box0_Out2 = 16;
const int Kitchen_Box0_Out3 = 17;

//Pins for outlets in BOX 1
const int Bedroom1_Box0_Out0 = 18;
const int Bedroom1_Box0_Out1 = 19;

const int Bedroom2_Box0_Out0= 21;
const int Bedroom2_Box0_Out1= 22;

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
  setup_pins();
}

void setup_pins(){
  //Set pins for box 0
  pinMode(Kitchen_Box0_Out0, OUTPUT);
  pinMode(Kitchen_Box0_Out1, OUTPUT);
  pinMode(Kitchen_Box0_Out2, OUTPUT);
  pinMode(Kitchen_Box0_Out3, OUTPUT);

  //Set pins for box 1
  pinMode(Bedroom1_Box0_Out0, OUTPUT);
  pinMode(Bedroom1_Box0_Out1, OUTPUT);
  
  pinMode(Bedroom2_Box0_Out0, OUTPUT);
  pinMode(Bedroom2_Box0_Out1, OUTPUT);

  //Set pins to low for box 0
  digitalWrite(Kitchen_Box0_Out0, LOW);
  digitalWrite(Kitchen_Box0_Out1, LOW);
  digitalWrite(Kitchen_Box0_Out2, LOW);
  digitalWrite(Kitchen_Box0_Out3, LOW);

  //Set pins to low for box 1
  digitalWrite(Bedroom1_Box0_Out0, LOW);
  digitalWrite(Bedroom1_Box0_Out1, LOW);
  
  digitalWrite(Bedroom2_Box0_Out0, LOW);
  digitalWrite(Bedroom2_Box0_Out1, LOW);  
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
