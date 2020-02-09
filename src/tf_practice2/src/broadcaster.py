#!/usr/bin/env python
import roslib
import rospy
import tf
import time
import math
import time

if __name__=='__main__':
    rospy.init_node('frame_a_frame_b_broadcaster_node')
    time.sleep(2)

    transform_broadcaster=tf.TransformBroadcaster()
    while(not rospy.is_shutdown()):
        rotation_quaternion=tf.transformations.quaternion_from_euler(0.2,0.3,0.1)
        translation_vector=(1.0,2.0,3.0)
        current_time=rospy.Time.now()
        transform_broadcaster.sendTransform(translation_vector,
            rotation_quaternion,current_time,'frame_b','frame_a')
        time.sleep(0.5)
    rospy.spin()