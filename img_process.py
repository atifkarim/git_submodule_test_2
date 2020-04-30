# !/home/atif/myenv/bin/python

import cv2

def do_gray(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
<<<<<<< HEAD
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return hsv
=======
    return img_gray


# This change I have done after adding submodule from my parent repo
>>>>>>> d2450deb844925e60a45ea766b47c5b5b0d2964a
