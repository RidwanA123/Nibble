
#include "HX711.h"
#include <LiquidCrystal.h>
#define DOUT 3
#define SCK 2

#define button 13

HX711 Scale;
int pirPin = 4;
int pirValue;
float offset = -680;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 9, d7 = 13;
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);


void setup() {
    lcd.begin(16, 2);
  // put your setup code here, to run once:
  Serial.begin(9600);
  Scale.begin(DOUT, SCK);
  pinMode(button, INPUT_PULLUP);
  pinMode(pirPin, INPUT);
  Scale.set_scale();
  Scale.tare();


  

}

void loop() {
pirValue = digitalRead(pirPin);
delay(100);
  Scale.set_scale(offset);
  // put your main code here, to run repeatedly:
  
if (digitalRead(button) == LOW) { //Reset Switch
  Scale.tare();
}
  
 if (pirValue == HIGH) { //Send Weight Information over Serial
  if (((int(Scale.get_units()))) >= 1) {
     Serial.print(Scale.get_units(), 1);
     
  }
 }
 
 lcd.setCursor(0,1);
 lcd.print(String(Scale.get_units()) + " LBS");

}
