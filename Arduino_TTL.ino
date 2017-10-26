int pushbutton = 9;
int output_pin = 13;
int pulse_width = 2;
int interval = 89;
int pushbutton_value;// value of pushbutton



void setup() {
  pinMode(output_pin, OUTPUT);
  Serial.begin(9600);
 //set LED (13) as output and open device at 9600 speed

}

void loop() {
  pushbutton_value = digitalRead(pushbutton);
  //read the value of the pushbutton
  if (pushbutton_value == HIGH){
    //if the pushbutton is pressed it will go to HIGH
    digitalWrite(output_pin, HIGH);
    Serial.println("1");
    //if pushbutton is pressed, turn LED "ON"
    delay(pulse_width);
    //keep LED "ON" for 2 millisec
    digitalWrite(output_pin, LOW);
    Serial.println("1");
    //then turn it "OFF" for 89 millisec
    //this will give you 12 frames per second
    delay(interval);
  }else{
     digitalWrite(output_pin, LOW);
     Serial.println("0");
    }
  }


