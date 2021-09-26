import RPi.GPIO as GPIO
import time


class AltAzimuth:
    def __init__(self, isWork, isHandDetected, handPos,
    servoUp = 8, servoDown = 7, windowWidth = 640, windowHeight = 480, calibration = 0.25):
        self.isWork = isWork
        self.isHandDetected = isHandDetected
        self.handPos = handPos

        self.posVertical = 40
        self.posHorizontal = 95

        #self.posVertical = 10
        #self.posHorizontal = 10

        self.SERVO_CENTER_VER = 85
        self.SERVO_CENTER_HOR = 85

        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.window_center_Width = int(self.windowWidth / 2)
        self.window_center_Heig = int(self.windowHeight / 2)

        self.window_calibration_Width = int(self.window_center_Width * calibration)
        self.window_calibration_Heig = int(self.window_center_Heig * calibration)

        self.timer = 5.0
        self.t = 0.0

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.servoUp = servoUp
        self.servoDown = servoDown

        GPIO.setup(self.servoUp, GPIO.OUT)
        GPIO.setup(self.servoDown, GPIO.OUT)

    def mainFunction(self):
        self.setAngle(self.servoUp,self.posVertical,0.2)
        time.sleep(0.1)
        self.setAngle(self.servoDown,self.posHorizontal,0.2)
        time.sleep(5)

        while self.isWork.value:
            if ((self.isHandDetected.value == 0) and (time.time() - self.t > self.timer)):
                self.searching()
            else:
                self.tracking()

    def setAngle(self, pin, angle, delay = 0.1):
        servo = GPIO.PWM(pin, 100)
        servo.start(0)
        dutyCycle = angle / 9.0 + 5
        servo.ChangeDutyCycle(dutyCycle)
        #print(f"angle = {angle}")
        time.sleep(0.05)
        servo.stop()
        time.sleep(delay)

    def tracking(self):

        while self.isHandDetected.value == 1:
            if (self.handPos[0] < (self.window_center_Width - self.window_calibration_Width) or
                self.handPos[0] > (self.window_center_Width + self.window_calibration_Width)):
                    #if ((self.handPos[0] > self.window_center_Width) and (self.posHorizontal < 170)):
                    if ((self.handPos[0] > self.window_center_Width)):
                        self.posHorizontal += 3
                        self.setAngle(self.servoDown,self.posHorizontal,0.1)
                        #time.sleep(1)
                    #elif(self.posHorizontal > 10):
                    else:
                        self.posHorizontal -= 3
                        self.setAngle(self.servoDown,self.posHorizontal,0.1)
                        #time.sleep(1)
                    print(f"track posHorizontal = {self.posHorizontal}")

            if (self.handPos[1] < (self.window_center_Heig - self.window_calibration_Heig) or
                self.handPos[1] > (self.window_center_Heig + self.window_calibration_Heig)):
                    #if ((self.handPos[1] > self.window_center_Heig) and (self.posVertical < 170)):
                    if ((self.handPos[1] > self.window_center_Heig)):
                        self.posVertical += 3
                        self.setAngle(self.servoUp,self.posVertical,0.1)
                        #time.sleep(1)
                    #elif(self.posVertical > 10):
                    else:
                        self.posVertical -= 3
                        self.setAngle(self.servoUp,self.posVertical,0.1)
                        #time.sleep(1)
                    print(f"track  posVertical = {self.posVertical}")



    def searching(self):
        directionVer = False
        directionHor = False

        while self.isHandDetected.value == 0:
            #==========================================================#

            if self.isHandDetected.value == 1: break

            while (self.posHorizontal > 10 and self.posHorizontal < 170):

                if self.isHandDetected.value == 1: break

                if directionHor == False:
                    self.posHorizontal += 2
                    self.setAngle(self.servoDown,self.posHorizontal,0.1)
                else:
                    self.posHorizontal -= 2
                    self.setAngle(self.servoDown,self.posHorizontal,0.1)
                    print(f"posHorizontal = {self.posHorizontal}")

            if self.isHandDetected.value == 1: break

            if directionHor == False:
                self.posHorizontal = 165
            else:
                self.posHorizontal = 15

            directionHor = not directionHor

            directionVer = not directionVer
            if directionVer == False:
                self.posVertical = 40
                self.setAngle(self.servoUp,self.posVertical,0.3)
            else:
                self.posVertical = 10
                self.setAngle(self.servoUp,self.posVertical,0.3)
                print(f"posVertical = {self.posVertical}")
            #==========================================================#

        self.t = time.time()
        print("End work - AltAzimuth.searching()")




    def __del__(self):
        GPIO.cleanup()



