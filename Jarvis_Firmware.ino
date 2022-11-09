#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
const int ledPin = 13; 

#include "BluetoothSerial.h"
#include "esp_bt_device.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif
// setting PWM properties
const int ledChannel = 0;
const int resolution = 8;
Adafruit_PWMServoDriver array1 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver array2 = Adafruit_PWMServoDriver(0x41);
int  B;
#define ONBOARD_LED  2
//Logic id numbs
//left
int LS = 0;
int LX = 10000;
int LY = 20000;
int LB = 30000;
int LW = 40000;
int LT = 50000;
int LI = 60000;
int LM = 70000;
int LR = 80000;
int LP = 90000;
//right
int RS = 100000;
int RXA = 110000;
int RY = 120000;
int RB = 130000;
int RW = 140000;
int RT = 150000;
int RI = 160000;
int RM = 170000;
int RR = 180000;
int RP = 190000;
//Extra
int HP = 200000;
int HT = 210000;
int JA = 220000;
int SP = 230000;
int Cap = 240000;
//channel ids
//left
int LSC = 0;
int LXC = 1;
int LYC = 2;
int LBC = 3;
int LWC = 4;
int LTC = 5;
int LIC = 6;
int LMC = 7;
int LRC = 8;
int LPC = 9;
//right
int RSC = 10;
int RXC = 11;
int RYC = 12;
int RBC = 13;
int RWC = 14;
int RTC = 15;
int RIC = 0;
int RMC = 1;
int RRC = 2;
int RPC = 7;
//Extra
int HPC = 4;
int HTC = 5;
int JAC = 6;
int freq = 0;
BluetoothSerial SerialBT;
void printDeviceAddress(){
  const uint8_t* point = esp_bt_dev_get_address();
  for (int l=0; l<6;l++){
    char str[3];
    sprintf(str, "%02x", (int)point[l]);
    Serial.print(str);
   if(1<5){
    Serial.print(":");
   }
  }
}
void setup() {
  Serial.begin(115200);
  Serial.println("System Ready");
  array1.begin();
  array1.setPWMFreq(60); 
  array1.setOscillatorFrequency(27000000);
  array2.begin();
  array2.setPWMFreq(60); 
  array2.setOscillatorFrequency(27000000);
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  Serial.print("BT Mac: ");
  printDeviceAddress();
  pinMode(ONBOARD_LED,OUTPUT);
}

void loop() {
  //obtaining data from comm port
  int B = SerialBT.parseInt(); 
  

  //Motor Movement Protocol
  //Left Shoulder
  if (B > LS && B < LX)
  {
    array1.setPWM(LSC, 0, (B - LS));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LS confirmed  ");
    //Serial.println(B - LS);
  }
  //Left X-arm
    if (B > LX && B < LY)
  {
    array1.setPWM(LXC, 0, (B - LX));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LX confirmed  ");
    //Serial.println(B - LX);
  }
  //Left Y-Arm
    if (B > LY && B < LB)
  {
    array1.setPWM(LYC, 0, (B - LY));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LY confirmed  ");
    //Serial.println(B - LY);
  }
  // Left Bicep
    if (B > LB && B < LW)
  {
    array1.setPWM(LBC, 0, (B - LB)); 
    //Serial.print("LB confirmed  ");
    //Serial.println(B - LB);  
  }
  // Left Wrist
    if (B > LW && B < LT)
  {
    array1.setPWM(LWC, 0, (B - LW)); 
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LW confirmed  ");
    //Serial.println(B - LW);  
  }
  // Left Thumb
    if (B > LT && B < LI)
  {
    array1.setPWM(LTC, 0, (B - LT));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW); 
    //Serial.print("LT confirmed  ");
    //Serial.println(B - LT);
  }
  // Left Index
    if (B > LI && B < LM)
  {
    array1.setPWM(LIC, 0, (B - LI));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LI confirmed  ");
    //Serial.println(B - LI);
  }
  // Left Middle
    if (B > LM && B < LR)
  {
    array1.setPWM(LMC, 0, (B - LM));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LM confirmed  ");
    //Serial.println(B - LM);  
  }
  // Left Ring
    if (B > LR && B < LP)
  {
    array1.setPWM(LRC, 0, (B - LR));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW); 
    //Serial.print("LR confirmed  ");
    //Serial.println(B - LR);  
  }
  // Left Pinky
    if (B > LP && B < RS)
  {
    array1.setPWM(LPC, 0, (B - LP));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("LP confirmed  ");
    //Serial.println(B - LP);
  }

//Right Arm Codex
  //Right Shoulder
  if (B > RS && B < RXA)
  {
    array1.setPWM(RSC, 0, (B - RS));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RS confirmed  ");
    //Serial.println(B - RS);
  }
  // Right X-arm
    if (B > RXA && B < RY)
  {
    array1.setPWM(RXC, 0, (B - RXA)); 
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RXA confirmed  ");
    //Serial.println(B - RXA);   
  }
  
  // Right Y-Arm
    if (B > RY && B < RB)
  {
    array1.setPWM(RYC, 0, (B - RY));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RY confirmed  ");
    //Serial.println(B - RY);  
  }
  // Right Bicep
    if (B > RB && B < RW)
  {
    array1.setPWM(RBC, 0, (B - RB)); 
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RB confirmed  ");
    //Serial.println(B - RB);  
  }
  // Left Wrist
    if (B > RW && B < RT)
  {
    array1.setPWM(RWC, 0, (B - RW));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RW confirmed  ");
    //Serial.println(B - RW);  
  }
  // Right Thumb
    if (B > RT && B < RI)
  {
    array1.setPWM(RTC, 0, (B - RT));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RT confirmed  ");
    //Serial.println(B - RT);   
  }
  // Right Index
    if (B > RI && B < RM)
  {
    array2.setPWM(RIC, 0, (B - RI));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RI confirmed  ");
    //Serial.println(B - RI); 
  }
  // Right Middle
    if (B > RM && B < RR)
  {
    array2.setPWM(RMC, 0, (B - RM));
    //Serial.print("RM confirmed  ");
    //Serial.println(B - RM);  
  }
  // Right Ring
    if (B > RR && B < RP)
  {
    array2.setPWM(RRC, 0, (B - RR));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RR confirmed  ");
    //Serial.println(B - RR);  
  }
  // Right Pinky
    if (B > RP && B < HP)
  {
    array2.setPWM(RPC, 0, (B - RP));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("RP confirmed  ");
    //Serial.println(B - RP);    
  }
// Head Movements
  // Head Pan
    if (B > HP && B < HT)
  {
    array2.setPWM(HPC, 0, (B - HP));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("HP confirmed  ");
    //Serial.println(B - HP);  
  }
  // Head Tilt
    if (B > HT && B < JA)
  {
    array2.setPWM(HTC, 0, (B - HT));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("HT confirmed  ");
    //Serial.println(B - HT);   
  }
  // Jaw
    if (B > JA && B < SP )
  {
    array2.setPWM(JAC, 0, (B - JA));
    delay(100);
    digitalWrite(ONBOARD_LED,HIGH);
    delay(100);
    digitalWrite(ONBOARD_LED,LOW);
    //Serial.print("JA confirmed  ");
    //Serial.println(B - JA); 
  }
  if (B > SP && B < Cap )
  {
    ledcSetup(ledChannel, freq, resolution);
    ledcAttachPin(ledPin, ledChannel);
    freq = (B-SP);
    ledcWrite(ledChannel, 75);
    //Serial.print("SP confirmed  ");
    //Serial.println(freq); 
  }
}
