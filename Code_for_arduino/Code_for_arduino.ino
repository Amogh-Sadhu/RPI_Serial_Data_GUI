char dataString[50];
int a =0; 
String user_data = ""; 
int data1 = 69; 
void setup() {
Serial.begin(9600);              //Starting serial communication
}
void loop() {
  user_data = Serial.readString();
  if(user_data.equals(":ACVOF,1#")){
    sprintf(dataString,":ACVOF,1,%d#",data1);
    Serial.println(dataString);
    }
  else{
    Serial.println("Command not recieved");
    }
delay(2000);
}
