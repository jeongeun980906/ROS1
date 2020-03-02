#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf

print('-----------------------------------------')
print('Roll-Pitch-Yaw Conversion to Quaternions')
print('-----------------------------------------')

roll=math.radians(90)
pitch=math.radians(0)
yaw=math.radians(0)

print 'roll = ', math.degrees(roll), 'pitch = ', math.degrees(pitch),'yaw = ', math.degrees(yaw)

quaternion=tf.transformations.quaternion_from_euler(roll,pitch,yaw)
print 'The resulting quaternion using "quaternion_from_euler" function: '
for i in range(4):
	print quaternion[i]
quaternion=[0.000870603531834,0.000870603531834,-0.546313138375,0.837579489778]
rpy = tf.transformations.euler_from_quaternion(quaternion)
roll_from_quaternion = rpy[0]
pitch_from_quaternion = rpy[1]
yaw_from_quaternion = rpy[2]

print('-----------------------------------------')
print 'convert back to roll-pitch-yaw using "euler_from_quaternion" function: '
print 'roll = ', math.degrees(roll_from_quaternion), 'pitch = ', math.degrees(pitch_from_quaternion),'yaw = ', math.degrees(yaw_from_quaternion)
print('we get the same initial roll-picth-roll values')
print('-----------------------------------------')

print('define a new quaternion manually as a list')
q=(0.707106781187,0.0,0.0,0.707106781187)

print('-----------------------------------------')
print 'convert back to roll-pitch-yaw using "euler_from_quaternion" function: '
print 'roll = ', math.degrees(roll_from_quaternion), 'pitch = ', math.degrees(pitch_from_quaternion),'yaw = ', math.degrees(yaw_from_quaternion)
print('-----------------------------------------')
print('you can change these values in the file to make other converions')