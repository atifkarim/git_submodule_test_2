# !/home/atif/myenv/bin/python

import cv2

def do_gray(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return img_gray


# This change I have done after adding submodule from my parent repo
