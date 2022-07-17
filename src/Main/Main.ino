
#include "HX711.h"
#include <LiquidCrystal.h>
#define DOUT 3
#define SCK 2



HX711 Scale;
int pirPin = 4;
int pirValue;
int button = 13;
float offset = -680;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 9, d7 = 13;
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);


void setup() {
    lcd.begin(16, 2);
  Serial.begin(9600);
  Scale.begin(DOUT, SCK);
  pinMode(button, INPUT_PULLUP);
  pinMode(pirPin, INPUT);
  Scale.set_scale();
  Scale.tare();

 long averageread = Scale.read_average(); 
  

}

void loop() {
pirValue = digitalRead(pirPin);

  Scale.set_scale(offset);
  
  

  
 if (pirValue == HIGH) { //Send Weight Information over Serial
  if (((int(Scale.get_units()))) >= 1) {
     Serial.println(Scale.get_units(), 1);
     
  }
 }
 
 lcd.setCursor(0,1);
 lcd.print(String(Scale.get_units()) + " LBS");
delay(1000);
}
