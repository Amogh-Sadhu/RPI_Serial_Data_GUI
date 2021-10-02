char dataString[50];
String user_data = ""; 
String Command_1 = ":ACVOF,1#";
String cmnd1  = ":ACVOF,1#";
String cmnd2  = ":ACVZ,1#";
String cmnd3  = ":ACVM,1#";
String cmnd4  = ":ACVOF,2#";
String cmnd5  = ":ACVZ,2#";
String cmnd6  = ":ACVM,2#";
String cmnd7  = ":DCVOF,1#";
String cmnd8  = ":DCVZ,1#";
String cmnd9  = ":DCVM,1#";
String cmnd10 = ":DCVOF,2#";
String cmnd11 = ":DCVZ,2#";
String cmnd12 = ":DCVM,2#";
int data1 = 50; 
void setup() {
Serial.begin(9600);              //Starting serial communication
}
void loop() 
{
  if(Serial.available())
  {
    user_data = Serial.readString();
    
    //Serial.println(user_data);
    if(user_data.equals(cmnd1))
    {
      sprintf(dataString,":ACVOF,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(user_data.equals(cmnd2))
    {
      sprintf(dataString,":ACVZ,1,%d#",data1);
      Serial.println(dataString);
    } 
    else if(user_data.equals(cmnd3))
    {
      sprintf(dataString,":ACVM,1,%d#",data1);
      Serial.println(dataString);
    } 
    else if(user_data.equals(cmnd4))
    {
      sprintf(dataString,":ACVOF,2,%d#",data1);
      Serial.println(dataString);
    } 
    else if(user_data.equals(cmnd5))
    {
      sprintf(dataString,":ACVZ,2,%d#",data1);
      Serial.println(dataString);
    } 
    else if(user_data.equals(cmnd6))
    {
      sprintf(dataString,":ACVM,2,%d#",data1);
      Serial.println(dataString);
    } 
    else if(user_data.equals(cmnd7))
    {
      sprintf(dataString,":DCVOF,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(user_data.equals(cmnd8))
    {
      sprintf(dataString,":DCVZ,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(user_data.equals(cmnd9))
    {
      sprintf(dataString,":DCVM,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(user_data.equals(cmnd10))
    {
      sprintf(dataString,":DCVOF,2,%d#",data1);
      Serial.println(dataString);
    }
    else if(user_data.equals(cmnd11))
    {
      sprintf(dataString,":DCVZ,2,%d#",data1);
      Serial.println(dataString);
    }
    else if(user_data.equals(cmnd12))
    {
      sprintf(dataString,":DCVM,2,%d#",data1);
      Serial.println(dataString);
    }
    else
    {
      Serial.println("Command not recieved");
    } 
    
    data1 = data1 + 1;
  }
}
