void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();
  //Controll outlets specified in topic
  //Box 0 Outlet 0
  if (String(topic) == "controll/Garage/Inside/outlets/outletbox_0/outlet_0") {
    if(messageTemp == "on"){
      Serial.println("Garage_Box0_Out0: ON");
      digitalWrite(Garage_Box0_Out0, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Garage_Box0_Out0: OFF");
      digitalWrite(Garage_Box0_Out0, LOW);
    }
  }
  //Box 0 Outlet 1
  else if (String(topic) == "controll/Garage/Inside/outlets/outletbox_0/outlet_1") {
    if(messageTemp == "on"){
      Serial.println("Garage_Box0_Out1: ON");
      digitalWrite(Garage_Box0_Out1, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Garage_Box0_Out1: OFF");
      digitalWrite(Garage_Box0_Out1, LOW);
    }
  }
  
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    
    //Create unique clientName
    String clientId = "ESP32-";
    clientId += building;
    clientId += zone;
    clientId += deviceName;
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Subscribe
      // Individual outlets under box 0
      client.subscribe("controll/Garage/Inside/outlets/outletbox_0/outlet_0");
      client.subscribe("controll/Garage/Inside/outlets/outletbox_0/outlet_1");
      
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
