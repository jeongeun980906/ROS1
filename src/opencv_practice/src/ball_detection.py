#!/usr/bin/env python
import numpy as np
import cv2

def read_rbg_image(image_name,show):
    rgb_image=cv2.imread(image_name)
    if show:
        cv2.imshow('RGB_image',rgb_image)
    return rgb_image

def filter_color(rgb_image,lower_bound_color,upper_bound_color):
    hsv_image=cv2.cvtColor(rgb_image,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image",hsv_image)

    yellowLower=(30,100,100)
    yellowUpper=(50,255,255)

    mask=cv2.inRange(hsv_image,lower_bound_color,upper_bound_color)

    return mask

def getContours(binary_image):
    _,contours,hierarchy=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    return contours

def process_contours(binary_image,rgb_image,contours):
    black_image=np.zeros([binary_image.shape[0],binary_image.shape[1],3],'uint8')

    for c in contours:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        if (area>100):
            cv2.drawContours(rgb_image,[c],-1,(150,250,250),1)
            cv2.drawContours(black_image,[c],-1,(150,250,150),1)
            cx,cy=get_contour_center(c)
            cv2.circle(rgb_image,(cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image,(cx,cy),int(radius),(0,0,255),1)
            cv2.circle(black_image,(cx,cy),2,(150,150,255),-1)
        print("Area:{}, preimeter={}".format(area,perimeter))
    print("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)
    cv2.imshow("Black Image Contours",black_image)

def get_contour_center(contour):
    M=cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
    return cx,cy


def main():
    image_name="/home/jhmbabo/catkin_ws/src/opencv_practice/src/image/tennisball03.jpg"
    rgb_image=read_rbg_image(image_name,True)
    yellowLower=(30,10,10)
    yellowUpper=(50,255,255)
    mask=filter_color(rgb_image,yellowLower,yellowUpper)
    cv2.imshow("mask",mask)
    countours=getContours(mask)
    process_contours(mask,rgb_image,countours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()