import numpy as np
import cv2

img=cv2.imread("/home/jhmbabo/catkin_ws/src/opencv_practice/src/image/blackwhite.jpg")

img

type(img) #numpy.ndarray
img.size #1350
img.shape #(15,30,3)
length=img.shape[0] #15
width=img.shape[1] #30
channel=img.shape[2] #30
img[:,:,0] #only first channel