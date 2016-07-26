int LEDPIN1 = 4;
int LEDPIN2 = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPIN1, LEDPIN2);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEDPIN1, HIGH);
  delay(20);
  digitalWrite(LEDPIN2, HIGH);
  delay(20);
}

