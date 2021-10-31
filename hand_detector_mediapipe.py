import cv2
import mediapipe as mp
import time


mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hand = mpHands.Hands(False, 1, 0.5, 0.5)

class handDetectorMediapipe():
    def __init__(self, isWork, isHandDetected, handPos,
    mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
        self.isWork = isWork
        self.isHandDetected = isHandDetected
        self.handPos = handPos

        #self.mode = mode
        #self.maxHands = maxHands
        #self.detectionCon = detectionCon
        #self.trackCon = trackCon

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = hand.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            self.isHandDetected.value = 1
            print(f"handDet (hand_detector_mediapipe) = {self.isHandDetected.value}")
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    mpDraw.draw_landmarks(img, handLms,
                                               mpHands.HAND_CONNECTIONS)
        else:
            self.isHandDetected.value = 0
            self.handPos[0] = -1
        return img

    def findPosition(self, img, handNo=0, draw=True):
        sumX = 0
        sumY = 0
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                #=========
                #print(f"lm.x = {lm.x}, lm.y = {lm.y}, lm.z = {lm.z}")
                #=========
                cx, cy = int(lm.x * w), int(lm.y * h)
                sumX += cx
                sumY += cy
                #=========
                #print(id, cx, cy)
                #=========
                #lmList.append([id, cx, cy])
                lmList.append([lm.x,lm.y,lm.z])

            self.handPos[0] = int(sumX/21)
            self.handPos[1] = int(sumY/21)
            cv2.circle(img, (self.handPos[0], self.handPos[1]), 5, (255, 0, 255), cv2.FILLED)

        return lmList