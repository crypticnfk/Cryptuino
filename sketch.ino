#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);

void setup()
{
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()) {
    delay(100);
    lcd.clear();
    lcd.setCursor(0, 0);
    while (Serial.available() > 0) {
      char ch = Serial.read();
      if(ch == '$') {
        lcd.setCursor(6,0);
      }
      lcd.print(ch);
      Serial.println(ch);
    }
  }
}
