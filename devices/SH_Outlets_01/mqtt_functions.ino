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
  if (String(topic) == "controll/home/livingroom/outlets/box_0/outlet_0") {
    if(messageTemp == "on"){
      Serial.println("Box0_Out0: ON");
      digitalWrite(Box0_Out0, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box0_Out0: OFF");
      digitalWrite(Box0_Out0, LOW);
    }
  }
  //Box 0 Outlet 1
  else if (String(topic) == "controll/home/livingroom/outlets/box_0/outlet_1") {
    if(messageTemp == "on"){
      Serial.println("Box0_Out1: ON");
      digitalWrite(Box0_Out1, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box0_Out1: OFF");
      digitalWrite(Box0_Out1, LOW);
    }
  }
  //Box 0 Outlet 2
  else if (String(topic) == "controll/home/livingroom/outlets/box_0/outlet_2") {
    if(messageTemp == "on"){
      Serial.println("Box0_Out2: ON");
      digitalWrite(Box0_Out2, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box0_Out2: OFF");
      digitalWrite(Box0_Out2, LOW);
    }
  }
  //Box 0 Outlet 3
  else if (String(topic) == "controll/home/livingroom/outlets/box_0/outlet_3") {
    if(messageTemp == "on"){
      Serial.println("Box0_Out3: ON");
      digitalWrite(Box0_Out3, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box0_Out3: OFF");
      digitalWrite(Box0_Out3, LOW);
    }
  }
  //Box 1 Outlet 0
  else if (String(topic) == "controll/home/livingroom/outlets/box_1/outlet_0") {
    if(messageTemp == "on"){
      Serial.println("Box1_Out0: ON");
      digitalWrite(Box1_Out0, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box1_Out0: OFF");
      digitalWrite(Box1_Out0, LOW);
    }
  }
  //Box 1 Outlet 1
  else if (String(topic) == "controll/home/livingroom/outlets/box_1/outlet_1") {
    if(messageTemp == "on"){
      Serial.println("Box1_Out1: ON");
      digitalWrite(Box1_Out1, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box1_Out1: OFF");
      digitalWrite(Box1_Out1, LOW);
    }
  }
  //Box 1 Outlet 2
  else if (String(topic) == "controll/home/livingroom/outlets/box_1/outlet_2") {
    if(messageTemp == "on"){
      Serial.println("Box1_Out2: ON");
      digitalWrite(Box1_Out2, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box1_Out2: OFF");
      digitalWrite(Box1_Out2, LOW);
    }
  }
  //Box 1 Outlet 3
  else if (String(topic) == "controll/home/livingroom/outlets/box_1/outlet_3") {
    if(messageTemp == "on"){
      Serial.println("Box1_Out3: ON");
      digitalWrite(Box1_Out3, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box1_Out3: OFF");
      digitalWrite(Box1_Out3, LOW);
    }
  }
  //Box 0 ALL outlets
  else if (String(topic) == "controll/home/livingroom/outlets/box_0/all") {
    if(messageTemp == "on"){
      Serial.println("Box_0_ALL: ON");
      digitalWrite(Box0_Out0, HIGH);
      digitalWrite(Box0_Out1, HIGH);
      digitalWrite(Box0_Out2, HIGH);
      digitalWrite(Box0_Out3, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box_0_ALL: OFF");
      digitalWrite(Box0_Out0, LOW);
      digitalWrite(Box0_Out1, LOW);
      digitalWrite(Box0_Out2, LOW);
      digitalWrite(Box0_Out3, LOW);
    }
  }
  //Box 1 ALL outlets
  else if (String(topic) == "controll/home/livingroom/outlets/box_1/all") {
    if(messageTemp == "on"){
      Serial.println("Box_1_ALL: ON");
      digitalWrite(Box1_Out0, HIGH);
      digitalWrite(Box1_Out1, HIGH);
      digitalWrite(Box1_Out2, HIGH);
      digitalWrite(Box1_Out3, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("Box_1_ALL: OFF");
      digitalWrite(Box1_Out0, LOW);
      digitalWrite(Box1_Out1, LOW);
      digitalWrite(Box1_Out2, LOW);
      digitalWrite(Box1_Out3, LOW);
    }
  }
  //ALL OUTLETS
  else if (String(topic) == "controll/home/livingroom/outlets/all") {
    if(messageTemp == "on"){
      Serial.println("ALL: ON");
      digitalWrite(Box0_Out0, HIGH);
      digitalWrite(Box0_Out1, HIGH);
      digitalWrite(Box0_Out2, HIGH);
      digitalWrite(Box0_Out3, HIGH);
      digitalWrite(Box1_Out0, HIGH);
      digitalWrite(Box1_Out1, HIGH);
      digitalWrite(Box1_Out2, HIGH);
      digitalWrite(Box1_Out3, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("ALL: OFF");
      digitalWrite(Box0_Out0, LOW);
      digitalWrite(Box0_Out1, LOW);
      digitalWrite(Box0_Out2, LOW);
      digitalWrite(Box0_Out3, LOW);
      digitalWrite(Box1_Out0, LOW);
      digitalWrite(Box1_Out1, LOW);
      digitalWrite(Box1_Out2, LOW);
      digitalWrite(Box1_Out3, LOW);
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
      client.subscribe("controll/home/livingroom/outlets/box_0/outlet_0");
      client.subscribe("controll/home/livingroom/outlets/box_0/outlet_1");
      client.subscribe("controll/home/livingroom/outlets/box_0/outlet_2");
      client.subscribe("controll/home/livingroom/outlets/box_0/outlet_3");

      // Individual outlets under box 1
      client.subscribe("controll/home/livingroom/outlets/box_1/outlet_0");
      client.subscribe("controll/home/livingroom/outlets/box_1/outlet_1");
      client.subscribe("controll/home/livingroom/outlets/box_1/outlet_2");
      client.subscribe("controll/home/livingroom/outlets/box_1/outlet_3");

      //Controll multiple outlets with one topic
      client.subscribe("controll/home/livingroom/outlets/box_0/all");
      client.subscribe("controll/home/livingroom/outlets/box_1/all");
      client.subscribe("controll/home/livingroom/outlets/all");
      
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
