#!/usr/bin/env python
#https://m.blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220517391218&proxyReferer=https%3A%2F%2Fwww.google.com%2F
import numpy as np
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import sys


bridge=CvBridge()

def filter_color(rgb_image,LowerBound,UpperBound):
    hsv_image=cv2.cvtColor(rgb_image,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv_image,LowerBound,UpperBound)
    return mask

def get_contours(binary_image):
    _,contours,hierachy=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours
'''
def get_contours_center(contour):
    M=cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
    return cx,cy
'''
def process_contours(rgb_image,binary_image,contours):
    black_image=np.zeros([rgb_image.shape[0],rgb_image.shape[1],3],'uint8')
    for c in contours:
        area=cv2.contourArea(c)
        x,y,w,h=cv2.boundingRect(c)
        if area>1000:
            cv2.drawContours(rgb_image,[c],-1,(0,255,255),2)
            cv2.drawContours(black_image,[c],-1,(0,255,255),2)
            cv2.rectangle(rgb_image,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.rectangle(black_image,(x,y),(x+w,y+h),(0,0,255),3)
            print("Area:{}".format(area))
    print("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)
    cv2.imshow("Black Image Contours",black_image)    

def image_callback(ros_image):
    print 'got an image'
    global bridge
    try:
        cv_image=bridge.imgmsg_to_cv2(ros_image,"bgr8")
    except CvBridgeError as e:
        print(e)
    cv2.imshow("RGBIMAGE",cv_image)
    (rows,cols,channels)=cv_image.shape
    yellowUpper=(30,100,100)
    yellowLower=(50,255,255)
    mask=filter_color(cv_image,yellowUpper,yellowLower)
    contours=get_contours(mask)
    process_contours(cv_image,mask,contours)
    cv2.waitKey(3)


def main(args):
    rospy.init_node("Image_converter",anonymous=True)
    image_sub=rospy.Subscriber("/usb_cam/image_raw",Image,image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "shutting down"
    cv2.destroyAllWindows()

if __name__=='__main__':
    main(sys.argv)