int LEDPIN = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPIN, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  tone(LEDPIN, 0);

}
