# importing the module

"""
Despite name, this is not the main file. This file was a test main file. There was an error that we consistently ran
into where if the hand went out of frame or the hand recognition API did not detect a hand, the program would freeze and
crash.
"""

import cv2
import mediapipe as mp
from secondHand import *
from part1 import *
from detectDistance import *
from EdgeDetector import *

import cv2
import pyrealsense2
import mediapipe as mp
import pytesseract

from realsense_depth import *
import numpy as np
from PIL import Image

#All the instantiate variables extracted from the other classes
realSenseDepthVar = DepthCamera()
#secondHandVar = secondHand()
readTextVar = extractText()
edgeDetectVar = EdgeDetector()

class mainFunction():


    # Excecute the class to extract characters from the menu if want to
    def executePart1Class(self):
        # Executed the function
        readTextVar.executeDriverFunction()

    # Excecute the detect distance class if we want to
    def executeDetectDistance(self):
        realSenseDepthVar.dummyMainForMainClass()

    #Excecute the edge detector class if we want to
    def executeEdgeDetector(self):
        edgeDetectVar.dummyMainForMainClass()


def main():
    # Initialize Camera Intel Realsense
    dc = DepthCamera()
    ret, depth_frame, color_frame = dc.get_frame()
    secondHandVar = secondHand()
    secondHandVar.gettingDistance(depth_frame, color_frame )
    secondHandVar.callHand(depth_frame, color_frame)

# driver function
if __name__ == "__main__":
    main()
