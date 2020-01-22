#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import math

def scan_callback(data):
    min_value,min_index=min_range_index(data.ranges)
    print "\nthe minimum range value is: ",min_value
    print "the minimum range index is: ",min_index

    max_value,max_index=max_range_index(data.ranges)
    print "\nthe maximum range value is: ",max_value
    print "the maximum range index is: ",max_index

    avarage_value=avarage_range(data.ranges)
    print "\nthe avarage range is: ",avarage_value

    avarage2=avarage_between_indicies(data.ranges,2,7)
    print "\nthe avarage between 2in dicies is: ",avarage2

def min_range_index(ranges):
    return (min(ranges),ranges.index(min(ranges)))

def max_range_index(ranges):
    ranges=[x for x in ranges if not math.isnan(x)]
    return (max(ranges),ranges.index(min(ranges)))

def avarage_range(ranges):
    ranges=[x for x in ranges if not math.isnan(x)]
    return sum(ranges)/float(len(ranges))

def avarage_between_indicies(ranges,i,j):
    ranges=[x for x in ranges if not math.isnan(x)]
    slice_of_array=ranges[i:j+1]
    return ( sum(slice_of_array)/float(len(slice_of_array)) )

if __name__ == '__main__':

    rospy.init_node('scan_node', anonymous=True)
    
    rospy.Subscriber("scan",LaserScan,scan_callback)

    rospy.spin()