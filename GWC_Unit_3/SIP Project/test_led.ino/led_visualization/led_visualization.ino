
#include <Adafruit_NeoPixel.h>    // include Adafruit library

/**INITIALIZE GLOBAL VARIABLES**/
const int MIC_PIN = A0;           // Mic sensor input in analog pin

#define REDPIN 9                  // number pins connected to Arduino
#define GREENPIN 10
#define BLUEPIN 11
 
void setup() {
  Serial.begin(9600);             // start the serial terminal
  
  //set the rgb pins as output
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
}

void loop(){
  int r=0, g=0, b=0;              // set the led strip to black

  //Read piezo ADC value in
  int micADC = analogRead(MIC_PIN); 
  Serial.println(micADC);         // so we can keep track of the led light (generate graph w values in Tools >> Serial Plotter)

  //set the led to change colors when a certain threshold is reached
  if (micADC > 27){
    r = 255; g=0; b=0;
  }
  else if (micADC > 18){
    r=0; g=255; b=0;
  }
  else if (micADC > 9){
    r=0; g=0; b=255;
  }

  //send the rgb values to the led
  analogWrite(REDPIN, r); 
  analogWrite(GREENPIN, g); 
  analogWrite(BLUEPIN, b); 

}
