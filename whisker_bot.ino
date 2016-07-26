#include<Servo.h>

/**
 * Whisker bot: Moves the robot forward until it hits something
 * then it turns until it can kepp moving forward
 * 
 * @author Hannah Noordeen, Rachel Ware, Julia Smith
 * @version July 21, 2016
 */
 
Servo servoRight;
Servo servoLeft;
int PIEZOPIN = 4;
int RIGHT_WHISKER_PIN = 7;
int LEFT_WHISKER_PIN = 5;
int clockwise = 1300;
int counter_clockwise = 1700;
int stationary = 1500;

void setup() {
  // put your setup code here, to run once:
  pinMode(PIEZOPIN, OUTPUT);
  pinMode(RIGHT_WHISKER_PIN, INPUT);
  pinMode(LEFT_WHISKER_PIN, INPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(stationary);
  servoRight.writeMicroseconds(stationary);  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(RIGHT_WHISKER_PIN) == 1 && digitalRead(LEFT_WHISKER_PIN) == 1)  //if whiskers aren't touching anything
    forward();
    
  if(digitalRead(RIGHT_WHISKER_PIN) != 1 && digitalRead(LEFT_WHISKER_PIN) != 1) //if both whiskers are touching somthing
  {
    tone(PIEZOPIN, 2000, 1000);
    backward();
    left(); //or right();
  }
  
  if(digitalRead(RIGHT_WHISKER_PIN) == 1 && digitalRead(LEFT_WHISKER_PIN) != 1)  //if the left whisker is touching something
  {
    tone(PIEZOPIN, 2000, 1000);
    backward();
    right();
  }
  
  else if(digitalRead(RIGHT_WHISKER_PIN) != 1 && digitalRead(LEFT_WHISKER_PIN) == 1)  //if the right whisker is touching something
  {
    tone(PIEZOPIN, 2000, 1000);
    backward();
    left();
  }
}

/**
 * Turns the wheels so the robot will turn left
 */
void left(){ 
  for (int x = 0; x<1; x++){
    servoLeft.writeMicroseconds (clockwise);
    delay(500);
  } 
}

/**
 * Turns the wheels so the robot will turn right
 */
void right(){  //turn right
  for (int x = 0; x<1;x++){
    servoRight.writeMicroseconds(counter_clockwise);
    delay(500);
  }
}

/**
 * Moves the robot backwards
 */
void backward() {  
  // put your main code here, to run repeatedly:
  for(int x = 0; x < 1; x++){
    servoRight.writeMicroseconds(clockwise);
    servoLeft.writeMicroseconds(counter_clockwise);
    delay(500);
  }
}

/**
 * Moves the robot forwards
 */
void forward() {  //move forward
  // put your main code here, to run repeatedly:
  for(int x = 0; x < 1; x++){
    servoRight.writeMicroseconds(counter_clockwise);
    servoLeft.writeMicroseconds(clockwise);
    delay(500);
  }
}
