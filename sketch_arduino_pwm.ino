#define MOTOR_SPEED_0 5
#define MOTOR_SPEED_1 6

void setup()
{
  pinMode(MOTOR_SPEED_0, OUTPUT);
  pinMode(MOTOR_SPEED_1, OUTPUT);


}

void loop() {
  analogWrite(MOTOR_SPEED_0, 80);
  analogWrite(MOTOR_SPEED_1, 80);

}
