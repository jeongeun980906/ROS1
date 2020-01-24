#!/usr/bin/env python
import numpy as np
import cv2

def read_rbg_image(image_name,show):
    rgb_image=cv2.imread(image_name)
    if show:
        cv2.imshow('RGB_image',rgb_image)
    return rgb_image

def convert_rgb_to_gray(rgb_image,show):
    gray_image=cv2.cvtColor(rgb_image,cv2.COLOR_BGR2GRAY)
    if show:
        cv2.imshow("Gray_image",gray_image)
    return gray_image

def convert_gray_to_binary(gray_image,adaptive,show):
    if adaptive:
        binary_image=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
    else:
        _,binary_image=cv2.threshold(gray_image,100,255,cv2.THRESH_BINARY)
    if show:
        cv2.imshow("binary_image",binary_image)
    return binary_image

def getContours(binary_image):
    _,contours,hierarchy=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    return contours

def process_contours(binary_image,rgb_image,contours):
    black_image=np.zeros([binary_image.shape[0],binary_image.shape[1],3],'uint8')

    for c in contours:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        if (area>10):
            cv2.drawContours(rgb_image,[c],-1,(150,250,250),1)
            cv2.drawContours(black_image,[c],-1,(150,250,150),1)
            cx,cy=get_contour_center(c)
            cv2.circle(rgb_image,(cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image,(cx,cy),int(radius),(0,0,255),1)
        print("Area:{}, preimeter={}".format(area,perimeter))
    print("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)
    cv2.imshow("Black Image Contours",black_image)

def get_contour_center(contour):
    #https://www.youtube.com/watch?v=AAbUfZD_09s
    M=cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
    return cx,cy


def main():
    image_name="/home/jhmbabo/catkin_ws/src/opencv_practice/src/image/tennisball01.jpg"
    rgb_image=read_rbg_image(image_name,True)
    gray_image=convert_rgb_to_gray(rgb_image,True)
    binary_image=convert_gray_to_binary(gray_image,True,True)
    countours=getContours(binary_image)
    process_contours(binary_image,rgb_image,countours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()