#!/usr/bin/env python

import numpy as np

import cv2

image_name="tree"
print("read an image from file")
color_image=cv2.imread("/home/jhmbabo/catkin_ws/src/opencv_practice/src/image/"+image_name+".jpg",cv2.IMREAD_COLOR)

print 'display image in native color'
cv2.imshow("original image",color_image)
cv2.moveWindow("original image",0,0)
print(color_image.shape)

height,width,channels=color_image.shape

print 'split the image into three channels'
blue,green,red=cv2.split(color_image)

cv2.imshow("Blue Channel",blue)
cv2.moveWindow("Blue Channel",width,height)

cv2.imshow("Red Channel",red)
cv2.moveWindow("Red Channel",2*width,height)

cv2.imshow("Green Channel",green)
cv2.moveWindow("Green Channel",3*width,height)

#HSV transfrom
print 'HSV'
hsv=cv2.cvtColor(color_image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
hsv_image=np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv image",hsv_image)

#gray scale
gray_image=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray scale",gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()