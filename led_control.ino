const int Pin = 3;
float voltage;
void setup()
{
  Serial.begin(9600);
  pinMode(Pin, OUTPUT);
}
void loop()
{
  while (Serial.available() > 0){
    int red = Serial.parseInt();
    if (Serial.read() == '\n') 
      {
           if(red<25){
            red = 25;
           }
           else if(red>200){
            red = 200;
           }
          voltage = map(red, 25, 250, 0, 255);
          analogWrite(Pin, voltage);
       }
    }
}
