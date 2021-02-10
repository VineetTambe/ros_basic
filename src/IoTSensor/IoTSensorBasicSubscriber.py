#!/usr/bin/env python
import rospy
from ros_basics.msg import IoTSensorBasic

def IoTSensor_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "I heard")
    rospy.loginfo("Id" + str(message.id))
    rospy.loginfo("Name" + str(message.name))
    rospy.loginfo("temp" + str(message.temp))
    rospy.loginfo("humidity" + str(message.humidity))

rospy.init_node('IoTSensorBasic_subscriber', anonymous=True)

rospy.Subscriber("IoTSensorBasic_topic", IoTSensorBasic, IoTSensor_callback)

rospy.spin()