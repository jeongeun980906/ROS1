#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <sstream>

using namespace std;
ros::Publisher velocity_publisher;
//method to move the robot straight
ros::Subscriber pose_subscriber;
turtlesim::Pose turtlesim_pose;

const double x_min=0.0;
const double y_min =0.0;
const double x_max=11.0;
const double y_max=11.0;

const double PI=3.14159265359;

void move(double speed, double distance, bool isForward);
void rotate(double angular_speed, double relative_angle,bool clockwise);
double degrees2radians(double angle_in_degrees);
double setDesiredOrientation (double desired_angle_radians);
void poseCallback(const turtlesim::Pose::ConstPtr & pose_message);
double getDistance(double x1,double y1, double x2, double y2);
void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance);
void gridClean();
void spiralClean();

int main(int argc,char **argv){
    ros::init(argc,argv,"turtlesim_cleaner");
    ros::NodeHandle n;
    velocity_publisher=n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",10);
    pose_subscriber=n.subscribe("/turtle1/pose",10,poseCallback);

    /*double speed;
    double distance;
    bool isForward;
    double angular_speed;
    double relative_angle;
    bool colockwise;

    cout<<"enter speed: ";
    cin>>speed;
    cout<<"enter distance: ";
    cin>>distance;
    cout<<"enter is Forward: ";
    cin>>isForward;

    move(speed,distance,isForward);

    cout<<"enter angular velocity(degree/sec): ";
    cin>>angular_speed;
    cout<<"enter dersired angle(degree): ";
    cin>>relative_angle;
    cout<<"clockwise? ";
    cin>>colockwise;

    rotate(degrees2radians(angular_speed),degrees2radians(relative_angle),colockwise);
    
    setDesiredOrientation(degrees2radians(120));*/

    ros::Rate loop(0.5);
    turtlesim::Pose pose;
    pose.x=1;
    pose.y=1;
    pose.theta=0;
    moveGoal(pose,0.01);

    //pose.x=6;
    //pose.y=5;
    //pose.theta=0;
    //moveGoal(pose,0.01);
    
    loop.sleep();

    //gridClean();
    spiralClean();
    
    ros::spin();

    return 0;
}

void move(double speed, double distance, bool isForward){
    //distance=speed*time
    geometry_msgs::Twist vel_msgs;

    if(isForward){
        vel_msgs.linear.x=abs(speed);
    }
    else {
        vel_msgs.linear.x=-abs(speed);
    }
    vel_msgs.linear.y=0;
    vel_msgs.linear.z=0;

    vel_msgs.angular.x=0;
    vel_msgs.angular.y=0;
    vel_msgs.angular.z=0; //only go straight

    //t0:current time
    double t0= ros::Time::now().toSec();
    double current_distance=0;
    ros::Rate loop_rate(10);

    do{
        velocity_publisher.publish(vel_msgs);
        double t1=ros::Time::now().toSec();
        current_distance=speed*(t1-t0);
        ros::spinOnce();
        loop_rate.sleep();
    }while(current_distance<distance);

    vel_msgs.linear.x=0;
    velocity_publisher.publish(vel_msgs);
}

void rotate(double angular_speed, double relative_angle,bool clockwise){
    geometry_msgs::Twist vel_msg;
    vel_msg.linear.x=0;
    vel_msg.linear.y=0;
    vel_msg.linear.z=0;

    vel_msg.angular.x=0;
    vel_msg.angular.y=0;
//initalize
    if(clockwise){
        vel_msg.angular.z=-abs(angular_speed);
    }
    else{
        vel_msg.angular.z=abs(angular_speed);
    }
    double current_angle=0;
    double t0= ros::Time::now().toSec();
    ros::Rate loop_rate(10);

    while(current_angle<relative_angle){
        velocity_publisher.publish(vel_msg);
         double t1=ros::Time::now().toSec();
        current_angle=angular_speed*(t1-t0);
        loop_rate.sleep();
        ros::spinOnce();
    }
    vel_msg.angular.z=0;
    velocity_publisher.publish(vel_msg);
}
double degrees2radians(double angle_in_degrees){
    return angle_in_degrees * PI/180.0;
}

double setDesiredOrientation (double desired_angle_radians){
    double relative_angle_radians=desired_angle_radians-turtlesim_pose.theta;
    bool clockwise=((relative_angle_radians<0)?true:false);
    //cout<<desired_angle_radians<<" ,"<<turtlesim_pose.theta<<","<<relative_angle_radians;
    rotate(abs(relative_angle_radians),abs(relative_angle_radians),clockwise);
}

void poseCallback(const turtlesim::Pose::ConstPtr & pose_message){
    turtlesim_pose.x=pose_message->x;
    turtlesim_pose.y=pose_message->y;
    turtlesim_pose.theta=pose_message->theta;
}
double getDistance(double x1,double y1, double x2, double y2){
    return sqrt(pow((x1-x2),2)+pow((y1-y2),2));
}

void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance){
    geometry_msgs::Twist vel_msg;
    ros::Rate loop_rate(10);

    while(getDistance(turtlesim_pose.x,turtlesim_pose.y,goal_pose.x,goal_pose.y)>distance_tolerance){
        vel_msg.linear.x=1.5*getDistance(turtlesim_pose.x,turtlesim_pose.y,goal_pose.x,goal_pose.y);
        vel_msg.linear.y=0;
        vel_msg.linear.z=0;

        vel_msg.angular.x=0;
        vel_msg.angular.y=0;
        vel_msg.angular.z=4*(atan2(goal_pose.y-turtlesim_pose.y,goal_pose.x-turtlesim_pose.x)-turtlesim_pose.theta);

        velocity_publisher.publish(vel_msg);

        ros::spinOnce();
        loop_rate.sleep();
    }
    cout<<"end"<<endl;
    vel_msg.linear.x=0;
    vel_msg.angular.z=0;
    velocity_publisher.publish(vel_msg);

}

void gridClean(){
    cout<<"girdcleaning"<<endl;
    ros::Rate loop(0.5);
    turtlesim::Pose pose;
    pose.x=1;
    pose.y=1;
    pose.theta=0;
    moveGoal(pose,0.01);
    loop.sleep();
    setDesiredOrientation(0);
    loop.sleep();

    move(2.0,9.0,true);
    loop.sleep();
    rotate(degrees2radians(10),degrees2radians(90),false);
    loop.sleep();
    move(2.0,9.0,true);
    
    rotate(degrees2radians(10),degrees2radians(90),false);
    loop.sleep();
    move(2.0,1.0,true);
    rotate(degrees2radians(10),degrees2radians(90),false);
    loop.sleep();
    move(2.0,9.0,true);

    rotate(degrees2radians(10),degrees2radians(90),false);
    loop.sleep();
    move(2.0,1.0,true);
    rotate(degrees2radians(10),degrees2radians(90),false);
    loop.sleep();
    move(2.0,9.0,true);
}

void spiralClean(){
    geometry_msgs::Twist vel_msg;
    double count=0;

    double constant_seed=4;
    double vk=1;
    double wk=2;
    double rk=0.5;
    ros::Rate loop(1);

    do{
        rk=rk+0.5;
        vel_msg.linear.x=rk;
        vel_msg.linear.y=0;
        vel_msg.linear.z=0;

        vel_msg.angular.x=0;
        vel_msg.angular.y=0;
        vel_msg.angular.z=constant_seed;

        velocity_publisher.publish(vel_msg);
        ros::spinOnce;

        loop.sleep();

    }while((turtlesim_pose.x<10.5)&&(turtlesim_pose.y<10.5));
    vel_msg.linear.x=0;
    velocity_publisher.publish(vel_msg);
}
