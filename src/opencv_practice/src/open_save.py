#!/usr/bin/env python

import numpy as np

import cv2

image_name='tree'

print 'read an image from file'
img=cv2.imread("/home/jhmbabo/catkin_ws/src/opencv_practice/src/image/"+image_name+".jpg")
#path to image

print 'create a window holder for the image'
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

print 'display the image'
cv2.imshow("Image",img)

print 'press a kery inside the image to make a copy'
cv2.waitKey(0)

print 'Imaged copied to a folder'
cv2.imwrite("image/copy/"+image_name+".copy.jpg",img)