# !/home/atif/myenv/bin/python

import cv2

def do_gray(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return hsv_1
    

# This change I have done after adding submodule from my parent repo
# total headbang stuffs
# changed now