#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

int main(int argc, char **argv){
    ros::init(argc, argv, "talker");
    ros::NodeHandle n;

    ros::Publisher chatter_pub= n.advertise<std_msgs::String>("chatter",1000);
    //register publisher
    ros::Rate loop_rate(1);//message per second

    int count=0;
    while (ros::ok()){
        std_msgs::String msg;

        std::stringstream ss;
        ss<<"hello world "<<count;
        msg.data=ss.str();

        ROS_INFO("[Talker] I published %s\n",msg.data.c_str());

        chatter_pub.publish(msg);//publish the message

        ros::spinOnce(); 

        loop_rate.sleep();
        ++count;
    }
    return 0;
    }