#include<Servo.h>

Servo servoRight;
Servo servoLeft;
int clockwise = 1300;
int counter_clockwise = 1700;
int stationary = 1500;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(stationary);
  servoRight.writeMicroseconds(stationary);  
}

void loop(){ //Left
  for (int x = 0; x<1; x++){
    servoLeft.writeMicroseconds (clockwise);
    delay(500);
  }
    servoLeft.writeMicroseconds(stationary);
 
}

void rloop(){  //Right
  for (int x = 0; x<1;x++){
    servoRight.writeMicroseconds(counter_clockwise);
    delay(500);
  }
    servoRight.writeMicroseconds(stationary);
}

void bloop() {  //backward
  // put your main code here, to run repeatedly:
  for(int x = 0; x < 1; x++){
    servoRight.writeMicroseconds(clockwise);
    servoLeft.writeMicroseconds(counter_clockwise);
    delay(500);
  }
   servoLeft.writeMicroseconds(stationary);
   servoRight.writeMicroseconds(stationary);
}

void floop() {  //forward
  // put your main code here, to run repeatedly:
  for(int x = 0; x < 1; x++){
    servoRight.writeMicroseconds(counter_clockwise);
    servoLeft.writeMicroseconds(clockwise);
    delay(500);
  }
   servoLeft.writeMicroseconds(stationary);
   servoRight.writeMicroseconds(stationary);
}
