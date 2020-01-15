#!/usr/bin/env python

import numpy as np
import cv2
#import imutils

image=cv2.imread("/home/jhmbabo/catkin_ws/src/opencv_practice/src/image/tennisball04.jpg")
cv2.imshow("original",image)

#convert image to HSV color space good for changes in external lightening source
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image",hsv)

#upper and lower bounds of the yellow color
yellowLower=(30,90,100)
yellowUpper=(60,255,255)

#define mask using the bounds
mask=cv2.inRange(hsv,yellowLower,yellowUpper)
cv2.imshow("mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()