import numpy as np
import cv2
import mediapipe as mp
import sys
import json
from multiprocessing import Process, Value, Array

import altazimuth
import hand_tracking
import neural_network

import RPi.GPIO as GPIO

# ================== tracking ================== #
def tracking():

    isWork = Value('b', True)
    isHandDetected = Value('b', False)
    handPos = Array('i', [-1,-1])

    altAz = altazimuth.AltAzimuth(isWork,isHandDetected,handPos)
    altAzProcess = Process(target=altAz.mainFunction)
    altAzProcess.start()

    handTrackingObj = hand_tracking.HandTracking(isWork,isHandDetected,handPos,32,640,480)
    handTrackingObj.mainFunctionTracking()

    isWork.value = False
    altAzProcess.join()
# ================== tracking ================== #


# ================== make_data ================== #
def make_data():
    isWork = Value('b', True)
    isHandDetected = Value('b', False)
    handPos = Array('i', [-1,-1])

    altAz = altazimuth.AltAzimuth(isWork,isHandDetected,handPos)
    altAzProcess = Process(target=altAz.mainFunction)
    altAzProcess.start()

    handTrackingObj = hand_tracking.HandTracking(isWork,isHandDetected,handPos,32,640,480)
    handTrackingObj.mainFunctionMakeData()

    isWork.value = False
    altAzProcess.join()
# ================== make_data ================== #


# ================== learning ================== #
def learning():
    data = []
    lenData = []
    currentNumb = []
    neuralNetwork = neural_network.NeuralNetwork(0.05, 42, 100, 100, 5)

    for numb in range(5):
        path = f"data/training_data/training_data_{numb}.json"
        with open(path, 'r') as f_out:
            data.append(json.load(f_out))
            lenData.append(len(data[numb]))
            currentNumb.append(0)

    for numbOfLearningData in range(25000):
        print(f"numbOfLearningData = {numbOfLearningData}")
        count = numbOfLearningData % 5
        print("count =", count)

        listLM = neural_network.getListLM(data[count][str(count)][currentNumb[count]])
        neuralNetwork.learning(listLM, count)
        currentNumb[count]+=1

        for i in range(5):
            if (currentNumb[i] == lenData[i]): currentNumb[i] = 0

    neuralNetwork.saveConfigurations()
# ================== learning ================== #

# ================== main ================== #

print(sys.argv)
if(len(sys.argv) == 1):
    sys.argv.append("")

if(sys.argv[1].lower() == "make_data"):
    print("Start in make_data-mode")
    make_data()

elif(sys.argv[1].lower() == "learning"):
    print("Start in learning-mode")
    learning()

elif(sys.argv[1].lower() == "tracking"):
    print("Start in tracking-mode")
    tracking()

else:
    print("Start in tracking-mode")
    tracking()

# ================== main ================== #