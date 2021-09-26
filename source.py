import numpy as np
import cv2
import mediapipe as mp
import sys
from multiprocessing import Process, Value, Array

import altazimuth
import hand_tracking

# ================== tracking ================== #
def tracking():

    #altAz = altazimuth.AltAzimuth()
    #altAz.mainFunction()
    isWork = Value('b', True)
    isHandDetected = Value('b', False)
    # handPos[0] is Xm handPos[1] is Y
    handPos = Array('i', [-1,-1])

    altAz = altazimuth.AltAzimuth(isWork,isHandDetected,handPos)
    altAzProcess = Process(target=altAz.mainFunction)
    altAzProcess.start()


    print("Here")
    handTrackingObj = hand_tracking.HandTracking(isWork,isHandDetected,handPos,32,640,480)
    handTrackingObj.mainFunction()

    isWork.value = False
    altAzProcess.join()



# ================== tracking ================== #


# ================== make_data ================== #
def make_data():
    pass
# ================== make_data ================== #


# ================== learning ================== #
def learning():
    pass
# ================== learning ================== #


# ================== main ================== #

print(sys.argv)
if(len(sys.argv) == 1):
    sys.argv.append("")

if(sys.argv[1].lower() == "make_data"):
    print("Start in make_data-mode")

elif(sys.argv[1].lower() == "learning"):
    print("Start in learning-mode")

elif(sys.argv[1].lower() == "tracking"):
    print("Start in tracking-mode")
    tracking()

else:
    print("Start in tracking-mode")
    tracking()

# ================== main ================== #