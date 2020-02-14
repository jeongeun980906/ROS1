#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal
from math import radians,degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def move_to_goal(Xgoal,Ygoal):
    ac=actionlib.SimpleActionClient("move_base",MoveBaseAction)
    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base_action server to come up")
    goal=MoveBaseGoal()
    goal.target_pose.header.frame_id='map'
    goal.target_pose.header.stamp=rospy.Time.now()

    goal.target_pose.pose.position=Point(Xgoal,Ygoal,0)
    goal.target_pose.pose.orientation.x=0.0
    goal.target_pose.pose.orientation.y=0.0
    goal.target_pose.pose.orientation.z=0.0
    goal.target_pose.pose.orientation.w=1.0

    rospy.loginfo("sending goal location ...")
    ac.send_goal(goal)
    ac.wait_for_result(rospy.Duration(60))
    if (ac.get_state())==GoalStatus.SUCCEEDED:
        rospy.loginfo("you have reached the destination")
        return True
    else:
        rospy.loginfo("The robot failed to reach the destination")
        return False
if __name__=='__main__':
    rospy.init_node('map_navigation',anonymous=False)
    x_goal=2.0
    y_goal=4.0
    print 'start go to goal'
    move_to_goal(x_goal,y_goal)
    rospy.spin()