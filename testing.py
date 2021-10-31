import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [26,19,13,6]

for pin in pins:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)

pwmPins = [20,21]
for pinPWM in pwmPins:
    print(pinPWM)
    GPIO.setup(pinPWM, GPIO.OUT)

rightWheelsSpeedPin = GPIO.PWM(pwmPins[0], 100)
leftWheelsSpeedPin = GPIO.PWM(pwmPins[1], 100)

rightWheelsSpeedPin.stop()
leftWheelsSpeedPin.stop()

GPIO.output(pins[0], GPIO.LOW)
GPIO.output(pins[1], GPIO.LOW)
GPIO.output(pins[2], GPIO.LOW)
GPIO.output(pins[3], GPIO.LOW)

time.sleep(2)

rightWheelsSpeedPin.start(0)
leftWheelsSpeedPin.start(0)

rightWheelsSpeedPin.ChangeDutyCycle(30)
leftWheelsSpeedPin.ChangeDutyCycle(30)

while True:
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.LOW)
    GPIO.output(pins[3], GPIO.HIGH)
    time.sleep(3)

    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)
    GPIO.output(pins[3], GPIO.LOW)
    time.sleep(3)






