#include "ros/ros.h"
#include "ros_tutorials_service/SrvTutorial.h"
#include <cstdlib>

int main(int argc, char **argv){
    ros::init(argc,argv,"service_client");
    if(argc !=3){
        ROS_INFO("cmd:rosrun rostutorials_service service_client arg0 arg1");
        ROS_INFO("arg0:double number, arg1: double number");
        return 1;
    }
    ros::NodeHandle nh;
    ros::ServiceClient ros_tutorials_service_client=nh.serviceClient<ros_tutorials_service::SrvTutorial>("ros_tutorials_srv");

    ros_tutorials_service::SrvTutorial srv;
    
    srv.request.a=atoll(argv[1]);
    srv.request.b=atoll(argv[2]);

    if(ros_tutorials_service_client.call(srv)){
        ROS_INFO("send srv, srv.Request.a and b: %1d %1d",(long int)srv.request.a, (long int)srv.request.b);
    }
    else{
        ROS_ERROR("Failed to call service ");
        return 1;
    }
    return 0;
}
