#!/usr/bin/env python

import numpy as np
import cv2
#import imutils
def getContours(binary_image):
    _,contours,hierarchy=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    return contours,hierarchy
def process_contours(rgb_image,binary_image,contours):
    black_image=np.zeros([rgb_image.shape[0],rgb_image.shape[1],3],'uint8')
    for c in contours:
        area=cv2.contourArea(c)
        x,y,w,h=cv2.boundingRect(c)
        if area>100:
            cv2.drawContours(rgb_image,[c],-1,(0,255,255),1)
            cv2.drawContours(black_image,[c],-1,(0,255,255),1)
            cv2.rectangle(rgb_image,(x,y),(x+w,y+h),(0,0,255),1)
            cv2.rectangle(black_image,(x,y),(x+w,y+h),(0,0,255),1)
            print("Area:{}".format(area))
    print("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)
    cv2.imshow("Black Image Contours",black_image)


image=cv2.imread("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/image_3.jpg")
image=cv2.resize(image,(540,540),interpolation=cv2.INTER_CUBIC)
cv2.imshow("original",image)

#convert image to HSV color space good for changes in external lightening source
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image",hsv)

#upper and lower bounds of the yellow color
yellowLower=(60,80,100)
yellowUpper=(80,250,255)

#define mask using the bounds
mask=cv2.inRange(hsv,yellowLower,yellowUpper)
cv2.imshow("mask",mask)

countours,hierachy=getContours(mask)
print(hierachy)
process_contours(image,mask,countours)

cv2.waitKey(0)
cv2.destroyAllWindows()