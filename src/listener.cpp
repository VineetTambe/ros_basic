#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("[Listener] I hear:[%s]\n",msg->data.c_str());
}


int main(int argc, char **argv)
{
    //Step1 initialize a new node named listener 
    ros::init(argc,argv,"listener");

    //Step2: create a node handler
    ros::NodeHandle node;

    //Step3: create a subscriber subscribing to the topic "chatter"
    ros::Subscriber sub = node.subscribe("chatter",1000,chatterCallback);

    //never forget this -> rosSpin will only process the buffer once vs ros spin will make an endless loop processing any messages coming to the callback function
    ros::spin();


    return 0;

}