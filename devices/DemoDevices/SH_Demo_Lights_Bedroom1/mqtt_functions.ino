
void callback(char* topic, byte* message, unsigned int length)
{
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  for (int i = 0; i < length; i++)
  {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

// Checks if new messages on esp32/ledstrip topic
// Changes ledstrip status based on message
  if (String(topic) == "controll/Home/Bedroom1/lights/light_0/pattern"){
    for(int i=0; i<LEDSHOW_COUNT; i++){
      if(messageTemp==ledshows[i]){
        ledshow=ledshows[i];
        loopflag = true;
        break;
      }}}
  else if(String(topic) == "controll/Home/Bedroom1/lights/light_0/status"){
    if(messageTemp == "off"){
      ledshow="allOff";
      loopflag = true;
    }
    else if(messageTemp == "on"){
      ledshow="allsame";
      loopflag = true;
    }}
  else if(String(topic) == "controll/Home/Bedroom1/lights/light_0/speed"){
    patternSpeed = messageTemp.toInt();
    loopflag = true;
  }
  else if(String(topic) == "controll/Home/Bedroom1/lights/light_0/color_0"){
    if(messageTemp == "red"){
      color_0_r = 127;
      color_0_g = 0;
      color_0_b = 0;
    }
    else if(messageTemp == "blue"){
      color_0_r = 0;
      color_0_g = 0;
      color_0_b = 255;
    }
    else if(messageTemp == "green"){
      color_0_r = 0;
      color_0_g = 255;
      color_0_b = 0;
    }loopflag = true;}
    
    else if(String(topic) == "controll/Home/Bedroom1/lights/light_0/color_1"){
    if(messageTemp == "red"){
      color_1_r = 127;
      color_1_g = 0;
      color_1_b = 0;
    }
    else if(messageTemp == "blue"){
      color_1_r = 0;
      color_1_g = 0;
      color_1_b = 255;
    }
    else if(messageTemp == "green"){
      color_1_r = 0;
      color_1_g = 255;
      color_1_b = 0;
    }loopflag = true;}
    
    else if(String(topic) == "controll/Home/Bedroom1/lights/light_0/color_2"){
    if(messageTemp == "red"){
      color_2_r = 127;
      color_2_g = 0;
      color_2_b = 0;
    }
    else if(messageTemp == "blue"){
      color_2_r = 0;
      color_2_g = 0;
      color_2_b = 255;
    }
    else if(messageTemp == "green"){
      color_2_r = 0;
      color_2_g = 255;
      color_2_b = 0;
    }loopflag = true;}
    
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    // Attempt to connect
    Serial.println("Attempting to connect to mqtt");

   //Create unique clientName
   String clientId = "ESP32-";
    clientId += building;
    clientId += zone;
    clientId += deviceName;
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      // Subscribe
      client.subscribe("controll/Home/Bedroom1/lights/light_0/status");
      client.subscribe("controll/Home/Bedroom1/lights/light_0/speed");
      client.subscribe("controll/Home/Bedroom1/lights/light_0/pattern");
      client.subscribe("controll/Home/Bedroom1/lights/light_0/color_0");
      client.subscribe("controll/Home/Bedroom1/lights/light_0/color_1");
      client.subscribe("controll/Home/Bedroom1/lights/light_0/color_2");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
