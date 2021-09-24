float number = 34.66413;
void setup(){
Serial.begin(9600);
}

void loop(){
    Serial.print(number,5);
    Serial.print("-");
    number=number+1.356;
    delay(2000);
    
}