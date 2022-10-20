#include <Adafruit_NeoPixel.h>

#define LED_PIN    5

#define LED_COUNT 144

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  Serial.println("<Arduino is ready>");
  strip.begin();          
  strip.show();            
  strip.setBrightness(50);
}

void loop() {
  if (Serial.available()) {  
    String command = Serial.readString();
    Serial.print(command);

    long starttime = millis();
    long endtime = starttime;
    while ((endtime - starttime) <=7900){
      strip.fill(strip.Color(0,0,255));
      strip.show();
      endtime = millis();
    }

    starttime = millis();
    endtime = starttime;
    while ((endtime - starttime) <=6100){
      strip.fill(strip.Color(255,69,0));
      strip.show();
      endtime = millis();
    }

    starttime = millis();
    endtime = starttime;
    while ((endtime - starttime) <=13500){
      strip.fill(strip.Color(139,0,0));
      strip.show();
      endtime = millis();
    }

    strip.fill(strip.Color(0,0,255));
    strip.show();
    
    if(command == "orange"){
      Serial.print("ORANGE");
      strip.fill(strip.Color(255,69,0));
      strip.show();
      colorWipe(strip.Color(255,69,0), 50); 
      colorWipe(strip.Color(245,59,0), 50); 
      colorWipe(strip.Color(235,49,0), 50); 
    }
    if(command == "grey"){
      Serial.print("GREY");
      strip.fill(strip.Color(255,69,0));
      strip.show();
      colorWipe(strip.Color(128,128,128), 50); 
      colorWipe(strip.Color(128,128,128), 50); 
      colorWipe(strip.Color(128,128,128), 50); 
    }
    if(command == "dark red"){
      Serial.print("DARK RED");
      strip.fill(strip.Color(139,0,0));
      strip.show();
      colorWipe(strip.Color(139,0,0), 50); 
      colorWipe(strip.Color(125,0,0), 50); 
      colorWipe(strip.Color(138,0,0), 50); 
    }
  }
}

void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) { 
    strip.setPixelColor(i, color);         
    strip.show();                     
    delay(100);             
  }
}
