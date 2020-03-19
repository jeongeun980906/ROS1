#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time
import math
from std_srvs.srv import Empty

def transformation(action):
    vel_msg=Twist()
    vel_msg.angular.y=0
    vel_msg.angular.x=0
    vel_msg.linear.z=0
    vel_msg.linear.y=0
    if action==0:
        vel_msg.linear.x=0.2
        vel_msg.angular.z=-0.23516
    elif action==1:
        vel_msg.linear.x=0.2
        vel_msg.angular.z=-0.144232 #right
    elif action==2:
        vel_msg.linear.x=0.2
        vel_msg.angular.z=0.0
    elif action==3:
        vel_msg.linear.x=-0.2
        vel_msg.angular.z=0.072116 #left
    elif action==4:
        vel_msg.linear.x=0.2
        vel_msg.angular.z=0.11758
    elif action==5:
        vel_msg.linear.x=-0.2
        vel_msg.angular.z=0.00
    elif action==6:
        vel_msg.linear.x=0.0
        vel_msg.angular.z=0.0
    return vel_msg
def move(action):
    velocity_publisher=rospy.Publisher('/cmd_vel',Twist,queue_size=100)
    vel_msg=transformation(action)
    loop_rate=rospy.Rate(100)
    for i in range(30):
        rospy.loginfo("moves")
        print(i)
        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()
    vel_msg=transformation(6)
    rospy.sleep(0.38)
    for i in range(10):
        rospy.loginfo('stop')
        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()
def odometry(action):
    x=0.0
    y=0.0
    w=0.0
    if action==0:
        x=0.048857
        y=-0.0091875
        w=-0.371747
    elif action==1:
        x=0.049046
        y=-0.008344
        w=-0.337109
    elif action==2:
        x=0.5
    elif action==3:
        x=0.049046
        y=0.008344
        w=0.337109
    elif action==4:
        x=0.048857
        y=0.0091875
        w=0.371747
    elif action==6:
        x=-0.05
    x_t=x*math.cos(w)-y*math.sin(w)
    y_t=x*math.sin(w)+y*math.cos(w)
    return x_t,y_t,w

if __name__ == "__main__":
    try:
        rospy.init_node('meekat_cmd_vel')
        velocity_publisher=rospy.Publisher('/cmd_vel',Twist,queue_size=100)
        action=[0,1,2,3,4,5]
        #action0:
        #print(action[1])
        move(action[0])
        #y: -0.151689540557
        rospy.sleep(5)
        reset=rospy.ServiceProxy('/gazebo/reset_world',Empty)
        reset()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")