#!/usr/bin/env python
PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)

import rospy 
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import cv2

def filter_color(rgb_image,lower_bound_color,upper_bound_color):
    hsv_image=cv2.cvtColor(rgb_image,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image",hsv_image)
    mask=cv2.inRange(hsv_image,lower_bound_color,upper_bound_color)
    return mask
def get_contours(binary_image):
    _,contours,hierachy=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours,hierachy

def largecontour(rgb_image,contours,hierarchy):        
    num=0
    for index,c in enumerate(contours):
        area=cv2.contourArea(c)
        x,y,w,h=cv2.boundingRect(c)

        if area>100:
            #cv2.drawContours(rgb_image,[c],-1,(0,255,255),1)
            #cv2.rectangle(rgb_image,(x,y),(x+w,y+h),(0,0,255),1)
            print index
            if hierarchy[0][index][3]==-1:
                print 'here'
                new_img=rgb_image[y:y+h,x:x+w]
            if hierarchy[0][index][3]==0:
                num=num+1
    print("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)

    cv2.imshow('new_img',new_img)
    return new_img,num
def smallcontour(rgb_image,contours,hierarchy,num):
    num_image=np.empty([num,28,28,3],'uint8')
    i=0
    for index,c in enumerate(contours):
        area=cv2.contourArea(c)
        x,y,w,h=cv2.boundingRect(c)
        if area>10:
            if hierarchy[0][index][3]==0:
                temp=rgb_image[y:y+h,x:x+w]
                print type(temp)
                temp=cv2.resize(temp,(28,28),interpolation=cv2.INTER_CUBIC)
                #cv2.imshow('temp',temp)
                num_image[i]=temp
                print(num_image.shape)
                i+=1
                print(i)
    #num_image=num_image[1:,:,:]
    
    print(num_image.shape)
    return num_image
def toBinary(img):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,binary_img=cv2.threshold(gray_img,107,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('binary',binary_img)
    return binary_img

def main():
    image_name="/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/image.jpg"
    img=cv2.imread(image_name)
    Lower=(0,0,0)
    Upper=(255,35,255)
    mask=filter_color(img,Lower,Upper)
    cv2.imshow('mask',mask)
    countours,hierarchy=get_contours(mask)
    #print(hierarchy)
    print type(img)
    new_img,num=largecontour(img,countours,hierarchy)
    cv2.imwrite("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/new_img.jpg",new_img)
    print 'number of numbers: ', num
    num_img=smallcontour(img,countours,hierarchy,num)
    for index,i in enumerate(num_img):
        print i,index
        print(i.shape)
        cv2.imshow('i',i)
        binary=toBinary(i)
        cv2.imwrite("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/num_image_"+str(index)+".jpg",binary)

    #handle(hierarchy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()