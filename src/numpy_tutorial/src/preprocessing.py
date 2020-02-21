#!/usr/bin/env python
PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)
import keras
import tensorflow as tf
import rospy 
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import cv2
import math
import copy

def filter_color(rgb_image,lower_bound_color,upper_bound_color):
    hsv_image=cv2.cvtColor(rgb_image,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image",hsv_image)
    mask=cv2.inRange(hsv_image,lower_bound_color,upper_bound_color)
    return mask
def get_contours(binary_image):
    _,contours,hierachy=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours,hierachy

def largecontour(rgb_image,contours,hierarchy):   
    #print(hierarchy)
    num=0
    new_img=[]     
    for index,c in enumerate(contours):
        area=cv2.contourArea(c)
        x,y,w,h=cv2.boundingRect(c)
        if area>200:
            #cv2.drawContours(rgb_image,[c],-1,(0,255,255),1)
            #cv2.rectangle(rgb_image,(x,y),(x+w,y+h),(0,0,255),1)
            print index
            if hierarchy[0][index][3]==-1:
                #print 'here'
                temp=rgb_image[y:y+h,x:x+w]
                temp=cv2.resize(temp,(160,160),interpolation=cv2.INTER_CUBIC)
                #cv2.imshow('temp',temp)
                new_img.append(temp)
                num+=1
    print("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)
    new_img_array=np.asarray(new_img)
    print(new_img_array.shape)
    return new_img_array,num

def smallcontour(rgb_image,contours,hierarchy,yanglist):
    num_image=[]
    x_index=[]
    #print(hierarchy)
    for index,c in enumerate(contours):
        area=cv2.contourArea(c)
        x,y,w,h=cv2.boundingRect(c)
        if area>100:
            for yang in yanglist:
                if hierarchy[0][index][3]==yang:
                    print(yang)
                    temp=rgb_image[y-10:y+h+10,x-10:x+w+10]
                    #cv2.imshow('temp',temp)
                    temp=cv2.resize(temp,(28,28),interpolation=cv2.INTER_AREA)
                    num_image.append(temp)
                    x_index.append(x)
                    print(type(num_image))
        #num_image=num_image[1:,:,:]
    num_image=np.array(num_image)
    print(num_image.shape)
    return num_image,x_index
    
def yangyang(hierarchy):
    yanglist=[]
    for i,h in enumerate(hierarchy[0]):
        if h[3]==-1:
            #print(i)
            if i==len(hierarchy[0])-1:
                continue
            else:
                if hierarchy[0][i+1][3]==-1:
                    continue
                else:
                    for j in range(10):
                        if j==0:
                            continue
                        if i+j>=len(hierarchy[0]):
                            break
                        else: 
                            if j==1:
                                temp=hierarchy[0][i+j][3]
                                yanglist.append(temp)
                            else:
                                if hierarchy[0][i+j][3]==-1:
                                    break
                                else:
                                    if hierarchy[0][i+j][3]<temp:
                                        yanglist.append(hierarchy[0][i+j][3])
                                    else: 
                                        continue
    return yanglist                  

def handle_hierarchy(hierarchy,contours,yanglist):
    hList=[]
    for index,c in enumerate(contours):
        area=cv2.contourArea(c)
        if area>100:
            hList.append(hierarchy[0][index][3])
    print(hList)
    fine_list=handle_hlist(hList,yanglist)
    return fine_list

def handle_hlist(hlist,yanglist):
    index=[]
    for i,h in enumerate(hlist):
        if h==-1:
            index.append(i)
    
    print('index',index)
    fine_list=[]
    count=0
    c2=0
    for j,k in enumerate(index):
        if j==0 and len(index)!=1:
            new_list=hlist[:index[j]]
        if j==0 and len(index)==1:
            new_list=hlist
        else:  
            new_list=hlist[index[j-1]:index[j]]
        print('new_list',new_list)
        
        for i in new_list:
            for y in yanglist:
                if i==y:
                    count+=1
        print count
        if (j==0 and len(index)!=1 and k!=0):
            fine_list.append(count)
        elif j==0 and len(index)==1:
            fine_list.append(count)
        elif j!=0:
            fine_list.append(count)    
            if j==len(index)-1:
                new_list2=hlist[index[j]:]
                print(new_list2)
                for i in new_list2:
                    for y in yanglist:
                        if i==y:
                            c2+=1
                print(c2)
                fine_list.append(c2)
    print(fine_list)
    return fine_list

def sunseo(x_index,fine_list):
    label=[]
    print(x_index)
    for i,f in enumerate(fine_list):
        temp_list=[0]*f
        if i==0:
            temp_x=x_index[:f]
        else:
            temp_x=x_index[fine_list[i-1]:f+fine_list[i-1]]
        print(temp_x)
        sort_x=copy.deepcopy(temp_x)
        sort_x.sort()
        sort_x.reverse()
        print(sort_x)
        print(type(sort_x))
        for a,x in enumerate(temp_x):
            for s,s_x in enumerate(sort_x):
                if s_x==x:
                    temp_list[a]=s
                    print(s)
        label.append(temp_list)
    print(label)
    return label

def toBinary(img):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,binary_img=cv2.threshold(gray_img,107,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow('binary',binary_img)
    return binary_img
def detection(fine_list,num_img,num,label):
    model=tf.keras.models.load_model('/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/num_classification.hdf5')
    prediction=model.predict(num_img)
    print(prediction)
    result=[0]*num
    if num==0:
        return result
    for n in range(num):
        print(n)
        print(fine_list[n])
        if n==0:
            temp_list=prediction[:fine_list[n]]
        else:
            temp_list=prediction[fine_list[n-1]:fine_list[n-1]+fine_list[n]]
        print(temp_list)
        for i,templist in enumerate(temp_list):
            if max(templist)<0.5:
                result[num-1-n]=0
            temp=np.argmax(templist)
            res=temp.item()
            #print(type(res))
            result[num-1-n]+=math.pow(10,label[n][i])*res
    print(result)
    return result

def main():
    image_name="/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/image_2.jpg"
    img=cv2.imread(image_name)
    img=cv2.resize(img,(540,540),interpolation=cv2.INTER_CUBIC)
    Lower=(60,80,100)
    Upper=(80,250,250)
    #Lower=(90,180,100)
    #Upper=(255,255,255)
    mask=filter_color(img,Lower,Upper)
    cv2.imshow('mask',mask)
    countours,hierarchy=get_contours(mask)
    print(hierarchy)
    yanglist=yangyang(hierarchy)
    print(yanglist)
    
    new_img_array,num=largecontour(img,countours,hierarchy)
    print(num)
    #new_img=new_img_array[0]
    #print(num)
    #print(new_img.shape)
    #cv2.imwrite("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/new_img.jpg",new_img)
    #for i,num_img in enumerate(new_img_array):
        #num_img=smallcontour(img,countours,hierarchy)
    #for index,i in enumerate(num_img):
        #print i,index
        #print(i.shape)
        #cv2.imshow('i',i)
        #binary=toBinary(i)
        #cv2.imwrite("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/num_image_"+str(index)+".jpg",binary)
    #for i,new_img in enumerate(new_img_array):
        #cv2.imwrite("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/new_img_"+str(i)+".jpg",new_img)
   
    num_img,x_index=smallcontour(img,countours,hierarchy,yanglist)
    fine_list=handle_hierarchy(hierarchy,countours,yanglist)
    label=sunseo(x_index,fine_list)
    print("finelist",fine_list)
    print(type(fine_list))
    new_num_image=np.zeros((len(num_img),28,28,1))
    #number=np.arange(1,num+1)
    for index,pix in enumerate(num_img):
        print(pix.shape)
        cv2.imshow('pix',pix)
        binary=toBinary(pix)
        cv2.imwrite("/home/jhmbabo/catkin_ws/src/numpy_tutorial/src/img/num_image_"+str(2*10+index)+".jpg",binary)
        binary=np.reshape(binary,(28,28,1))
        #print(binary.shape)
        new_num_image[index]=binary
        #print(new_num_image.shape)
    result=detection(fine_list,new_num_image,num,label)
    #handle(hierarchy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()