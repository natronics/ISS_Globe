#include <Servo.h> 

/* Pin outs */
#define LATITUDE     9
#define LONGITUDE   10
#define LASER       12
#define POWER_LED   11

/* States */
int channel1 = false;
int channel2 = false;
int laserState = HIGH;
int commandChar = 0;

/* Servos */
Servo lat_servo;
Servo lon_servo;

/* Init */
void setup()
{
  // Begin USB serial connection
  Serial.begin(57600);
  
  // Initilize servos
  lat_servo.attach(LATITUDE );
  lon_servo.attach(LONGITUDE);
  
  // Initilize ports
  pinMode(LASER    , OUTPUT);
  pinMode(POWER_LED, OUTPUT);
  
  // Being with laser off 
  digitalWrite(LASER, HIGH);
  
  // Leave a tiny amount of time for OCD compliance 
  // Turn on power indacator.
  delay(10);
  digitalWrite(POWER_LED, HIGH);
}

void loop()
{
  if (Serial.available()) {
    
    commandChar = Serial.read();
    
    if (channel1 == true)
    {
      lat_servo.write(commandChar);
      channel1 = false;
    }
    else if (channel2 == true)
    {
      lon_servo.write(commandChar);
      channel2 = false;
    }
    else
    {
      if (commandChar == 112)     // p
        channel1 = true;
      else if (commandChar == 108) // l
        channel2 = true;
      else if  (commandChar == 115) // s
        toggle_laser();
    }
  }
}

void toggle_laser()
{
  if (laserState == LOW)
  {
    digitalWrite(LASER, HIGH);
    laserState = HIGH;
  }
  else
  {
    digitalWrite(LASER, LOW);
    laserState = LOW;
  }
}
