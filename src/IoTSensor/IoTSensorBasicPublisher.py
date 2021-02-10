#!/usr/bin/env python
# license removed for brevity
import rospy
from ros_basics.msg import IoTSensorBasic

pub = rospy.Publisher('IoTSensorBasic_topic', IoTSensorBasic, queue_size=10)

rospy.init_node('IoTSensorBasic_publisher', anonymous=True)

rate = rospy.Rate(1) # 1hz
i = 0
while not rospy.is_shutdown():
    iot = IoTSensorBasic()
    iot.id = i
    iot.name = "IoTSensor"+str(i)
    iot.temp = 23.0
    iot.humidity = 100.0

    rospy.loginfo("[Publisher]:")
    rospy.loginfo(iot)

    pub.publish(iot)
    rate.sleep()
    i=i+1