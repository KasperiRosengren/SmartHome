#include <WiFi.h>
#include <PubSubClient.h>
#include <FastLED.h>
#define LED_PIN     4
#define NUM_LEDS    72
CRGB leds[NUM_LEDS];

// Replace the next variables with your SSID/Password combination
const char* ssid = "SSID";
const char* password = "PASSWORD";

// Give your MQTT server addres
const char* mqtt_server = "192.168.0.106";
const int mqtt_server_port = 2883;

String building = "Home";
String zone = "Bedroom1";
String deviceName = "lights";

bool loopflag = true;

// Task handles for multithreading
TaskHandle_t Task1;
TaskHandle_t Task2;

//WiFiClient espClient;
WiFiClient clientname;
PubSubClient client(clientname);
long lastMsg = 0;
char msg[50];
int value = 0;


//Define how many ledshow options there are
//and put all of their names in array
#define LEDSHOW_COUNT 3
String ledshows[LEDSHOW_COUNT] = {"allsame", "backandforth", "chase"};


String ledshow = "";
String lastledshow = "none";

//Set first color default to Blue
int color_0_r = 0;
int color_0_g = 0;
int color_0_b = 255;

//Set second color default to Red
int color_1_r = 127;
int color_1_g = 0;
int color_1_b = 0;

//Set third color default to green
int color_2_r = 0;
int color_2_g = 255;
int color_2_b = 0;

int patternSpeed = 100;


void setup() {
  Serial.begin(115200);
  setup_wifi();   //Tries to connect to wifi, if does not succed try again in 0,5s
  client.setServer(mqtt_server, mqtt_server_port);    //Set the mqtt broker connection info, use variables from earlier
  client.setCallback(callback);   //Set the function name where to send the subscribed topics message
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);    //Setup the ledstrip
  create_core_tasks();    //Create tasks for both cores and pin them to them
}

void create_core_tasks(){
  delay(10);
  //create a task that will be executed in the Task1code() function, with priority 1 and executed on core 0
  xTaskCreatePinnedToCore(
    Task1code,   /* Task function name. */
    "Task1",     /* name of task. */
    10000,       /* Stack size of task */
    NULL,        /* parameter of the task */
    1,           /* priority of the task */
    &Task1,      /* Task handle to keep track of created task */
    0);          /* pin task to core 0 */                  
  delay(500); //Wait for 0.5s

  //create a task that will be executed in the Task2code() function, with priority 1 and executed on core 1
  xTaskCreatePinnedToCore(
    Task2code,   /* Task function name. */
    "Task2",     /* name of task. */
    10000,       /* Stack size of task */
    NULL,        /* parameter of the task */
    1,           /* priority of the task */
    &Task2,      /* Task handle to keep track of created task */
    1);          /* pin task to core 1 */
  delay(500); 
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

//Task1code: Run mqtt client
void Task1code( void * pvParameters ){
  while(true){
    if (!client.connected()){
      reconnect();
    }
    client.loop();
    vTaskDelay(20);
  } 
}

//Task2code: run led strip
void Task2code( void * pvParameters ){
  while(true){
    ledstripmain();
  }
}

void loop(){}
