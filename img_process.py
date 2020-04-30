# !/home/atif/myenv/bin/python

import cv2

def do_gray(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return hsv

# This change I have done after adding submodule from my parent repo
