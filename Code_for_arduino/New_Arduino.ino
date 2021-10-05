char dataString[50];
String user_data = ""; 

String cmnd1  = "ACVOF";
String cmnd2  = "ACVZ";
String cmnd3  = "ACVM";
String cmnd4  = "ACVOF";
String cmnd5  = "ACVZ";
String cmnd6  = "ACVM";
String cmnd7  = "DCVOF";
String cmnd8  = "DCVZ";
String cmnd9  = "DCVM";
String cmnd10 = "DCVOF";
String cmnd11 = "DCVZ";
String cmnd12 = "DCVM";
String cmnd13  = "PF";
String cmnd14  = "ACW";
String cmnd15  = "DCW";
String cmnd16  = "EFP";
String cmnd17  = "ARSL";
String cmnd18  = "SVS";
int data1 = 50; 
/*..............................................................................................................*/

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
/*..............................................................................................................*/
void setup() {
Serial.begin(9600);              //Starting serial communication
}
/*..............................................................................................................*/
void loop() 
{
  if(Serial.available())
  {
    user_data = Serial.readString();
    //Serial.println(user_data);
    String data = user_data.substring(":", ",");
  
    String cmnd_temp = getValue(user_data, ',', 0);
    String cmnd_str = getValue(cmnd_temp,':',1);
    String ch_str = getValue(user_data, ',', 1);
    String data_str = getValue(user_data,',',2);
    int len = data_str.length();
    int hash_loc = data_str.indexOf("#");
    data_str.remove(hash_loc);
    
    //Serial.println("Command = " + cmnd_str);
    //Serial.println("Channel = "+ ch_str);
    //Serial.println("Data = "+data_str);

    if(cmnd_str.equals(cmnd1))
    {
      sprintf(dataString,":ACVOF,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd2))
    {
      sprintf(dataString,":ACVZ,1,%d#",data1);
      Serial.println(dataString);
    } 
    else if(cmnd_str.equals(cmnd3))
    {
      sprintf(dataString,":ACVM,1,%d#",data1);
      Serial.println(dataString);
    } 
    else if(cmnd_str.equals(cmnd4))
    {
      sprintf(dataString,":ACVOF,2,%d#",data1);
      Serial.println(dataString);
    } 
    else if(cmnd_str.equals(cmnd5))
    {
      sprintf(dataString,":ACVZ,2,%d#",data1);
      Serial.println(dataString);
    } 
    else if(cmnd_str.equals(cmnd6))
    {
      sprintf(dataString,":ACVM,2,%d#",data1);
      Serial.println(dataString);
    } 
    else if(cmnd_str.equals(cmnd7))
    {
      sprintf(dataString,":DCVOF,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd8))
    {
      sprintf(dataString,":DCVZ,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd9))
    {
      sprintf(dataString,":DCVM,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd10))
    {
      sprintf(dataString,":DCVOF,2,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd11))
    {
      sprintf(dataString,":DCVZ,2,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd12))
    {
      sprintf(dataString,":DCVM,2,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd13))
    {
      sprintf(dataString,":PF,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd14))
    {
      sprintf(dataString,":ACW,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd15))
    {
      sprintf(dataString,":DCW,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd16))
    {
      sprintf(dataString,":EFP,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd17))
    {
      sprintf(dataString,":ARSL,2#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd18))
    {
      sprintf(dataString,":SVS,2#");
      Serial.println(dataString);
    }
    else
    {
      Serial.println("Command not recieved");
    } 
    
    data1 = data1 + 1;
  }  
}
