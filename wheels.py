import RPi.GPIO as GPIO
import time

class Wheels:
    def __init__(self, pinsList, pwmPinsList):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.pins = pinsList
        self.pinsEnable = pwmPinsList

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        for pin in self.pinsEnable:
            GPIO.setup(pin, GPIO.OUT)

        GPIO.output(self.pins[0], GPIO.LOW)
        GPIO.output(self.pins[1], GPIO.LOW)
        GPIO.output(self.pins[2], GPIO.LOW)
        GPIO.output(self.pins[3], GPIO.LOW)

    def move(self, numbOfgesture):
        if numbOfgesture == 0:
            GPIO.output(self.pins[0], GPIO.HIGH)
            GPIO.output(self.pins[1], GPIO.LOW)
            #GPIO.output(self.pins[2], GPIO.LOW)
            #GPIO.output(self.pins[3], GPIO.HIGH)
        elif numbOfgesture == 1:
            GPIO.output(self.pins[0], GPIO.HIGH)
            GPIO.output(self.pins[1], GPIO.LOW)
            GPIO.output(self.pins[2], GPIO.HIGH)
            GPIO.output(self.pins[3], GPIO.LOW)
        elif numbOfgesture == 2:
            #GPIO.output(self.pins[0], GPIO.LOW)
            #GPIO.output(self.pins[1], GPIO.HIGH)
            GPIO.output(self.pins[2], GPIO.HIGH)
            GPIO.output(self.pins[3], GPIO.LOW)
        elif numbOfgesture == 3:
            GPIO.output(self.pins[0], GPIO.LOW)
            GPIO.output(self.pins[1], GPIO.HIGH)
            GPIO.output(self.pins[2], GPIO.LOW)
            GPIO.output(self.pins[3], GPIO.HIGH)
        elif numbOfgesture == 4:
            GPIO.output(self.pins[0], GPIO.LOW)
            GPIO.output(self.pins[1], GPIO.LOW)
            GPIO.output(self.pins[2], GPIO.LOW)
            GPIO.output(self.pins[3], GPIO.LOW)

            #####
            #####
            #####
            #return 0
        else:
            GPIO.output(self.pins[0], GPIO.LOW)
            GPIO.output(self.pins[1], GPIO.LOW)
            GPIO.output(self.pins[2], GPIO.LOW)
            GPIO.output(self.pins[3], GPIO.LOW)