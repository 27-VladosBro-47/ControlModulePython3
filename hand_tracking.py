import cv2
import json
import os
from picamera.array import PiRGBArray
from picamera import PiCamera

import hand_detector_mediapipe as HandDetector
import neural_network

class HandTracking:

    def __init__(self, isWork, isHandDetected, handPos, framerate, widthImg, heightImg):
        self.isWork = isWork
        self.isHandDetected = isHandDetected
        self.handPos = handPos

        self.widthImg = widthImg
        self.heightImg = heightImg

        # Capture the camera
        self.cam = PiCamera()
        self.cam.resolution = (widthImg, heightImg)
        self.cam.framerate = framerate
        self.rawCapture = PiRGBArray(self.cam, size=(widthImg, heightImg))

        # Initialization Hand Detector
        self.handDetector = HandDetector.handDetectorMediapipe(isWork,isHandDetected,handPos)

        self.neuralNetwork = neural_network.NeuralNetwork.createFromConfigFile()

        cv2.waitKey(100)

    def mainFunctionTracking(self):

        for frame in self.cam.capture_continuous(self.rawCapture, format="bgr",
        use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            img = frame.array
            img = cv2.flip(img, 0)

            img = self.handDetector.findHands(img)
            handLM = self.handDetector.findPosition(img)

            handLM = neural_network.getListLM(handLM)
            if not (len(handLM) == 0):
                result = self.neuralNetwork.work(handLM)
                cv2.putText(img, str(result), (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

            cv2.imshow("Video", img)

            if(cv2.waitKey(1) & 0xFF == ord("q")):
                self.isWork.value = False
                break

            # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)

    def mainFunctionMakeData(self):

        for frame in self.cam.capture_continuous(self.rawCapture, format="bgr",
        use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            img = frame.array
            img = cv2.flip(img, 0)

            img = self.handDetector.findHands(img)
            handLM = self.handDetector.findPosition(img)

            if (len(handLM)) != 0:
                self.saveHandLM(handLM)

            cv2.imshow("Video", img)

            if(cv2.waitKey(1) & 0xFF == ord("q")):
                self.isWork.value = False
                break

            # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)



    def saveHandLM(self, lm):
        if (cv2.waitKey(1) & 0xFF == ord("0")):
            self.updateTrainDataFile(0, lm)
        elif (cv2.waitKey(1) & 0xFF == ord("1")):
            self.updateTrainDataFile(1, lm)
        elif (cv2.waitKey(1) & 0xFF == ord("2")):
            self.updateTrainDataFile(2, lm)
        elif (cv2.waitKey(1) & 0xFF == ord("3")):
            self.updateTrainDataFile(3, lm)
        elif (cv2.waitKey(1) & 0xFF == ord("4")):
            self.updateTrainDataFile(4, lm)

    def updateTrainDataFile(self, gesture, lm):
        path = f"data/test_training_data/training_data_{gesture}.json"
        data = {}

        if (not (os.path.isfile(path))) or (os.stat(path).st_size == 0):
            with open(path, 'w') as f:
                data[str(gesture)] = []
                json.dump(data, f, indent=2)

        with open(path, 'r') as f:
            data = json.load(f)

        with open(path, 'w') as f:
            data[str(gesture)].append(lm)
            json.dump(data, f, indent=2)
            print("Data has been created!")

        cv2.waitKey(1000)




