#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    //Step1: create a new ros node name talker
    ros::init(argc,argv,"talker");

    //Step2: create a node handle reference to your node
    ros::NodeHandle n;

    //Step3: Create the publisher
    ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("chatter",1000);

    //we haven't started publishing yet

    //in order to create some delay in the loop-> 1 Hz 
    ros::Rate loop_rate(2.0); //->1 message /sec

    int count =0;
    while(ros::ok()) // better than while true
    {
        //create a message to be published
        std_msgs::String msg;

        std::stringstream ss;
        ss<<"hello there "<< count;

        msg.data = ss.str();

        //printing it to the log screen
        ROS_INFO("[Talker] I published %s\n", msg.data.c_str());

        //actually publishing the message
        chatter_publisher.publish(msg);

        ros::spinOnce(); // it allows to send all message in the buffer -> message will be processed and effectively published

        loop_rate.sleep(); //delay
        count++;

    }
    return 0;

}