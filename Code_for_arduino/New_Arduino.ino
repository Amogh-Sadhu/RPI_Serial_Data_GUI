char dataString[50];
String user_data = ""; 

String cmnd1  = "ACVOF";
String cmnd2  = "ACVZ";
String cmnd3  = "ACVM";
String cmnd4  = "DCVOF";
String cmnd5  = "DCVZ";
String cmnd6  = "DCVM";
String cmnd7  = "PF";
String cmnd8  = "ACW";
String cmnd9  = "DCW";
String cmnd10  = "EFP";
String cmnd11  = "ARSL";
String cmnd12  = "SVS";
int  data1 = 1; 
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
      sprintf(dataString,":DCVOF,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd5))
    {
      sprintf(dataString,":DCVZ,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd6))
    {
      sprintf(dataString,":DCVM,1,%d#",data1);
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd7))
    {
      sprintf(dataString,":PF,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd8))
    {
      sprintf(dataString,":ACW,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd9))
    {
      sprintf(dataString,":DCW,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd10))
    {
      sprintf(dataString,":EFP,1#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd11))
    {
      sprintf(dataString,":ARSL,2#");
      Serial.println(dataString);
    }
    else if(cmnd_str.equals(cmnd12))
    {
      sprintf(dataString,":SVS,2#");
      Serial.println(dataString);
    }
    else
    {
      Serial.println("Command not recieved");
    } 
    
    data1 = data1 + 1.045;
  }  
}
