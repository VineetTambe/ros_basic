#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
import math
import time

x_coord=0.0
y_coord=0.0
theta_coord=0.0


def pose_callback(pose_msg):
    #updating global variables
    global x_coord,y_coord,theta_coord
    
    x_coord=pose_msg.x
    y_coord=pose_msg.y
    
    theta_coord=pose_msg.theta
    #rospy.loginfo("[Publishing] in pose callback ")
    #rospy.loginfo("[Publishing] x "+str(x_coord))
    #rospy.loginfo("[Publishing] y "+str(y_coord))
    
    

def move_turtle(goal_distance, speed):

    #step1 initial vel_msg
    vel_msg = Twist()

    #step2 declare a publisher node
    speed_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    #step3 initialize distance variables
    x_ini=x_coord
    y_ini=y_coord

    #set the loop rate
    rate = rospy.Rate(10) # 10hz
    distance = 0.0
    #keep publishing until a Ctrl-C is pressed
    vel_msg.linear.x = speed
    rospy.loginfo("[Publishing] linear x = "+str(vel_msg.linear.x))
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % i
        vel_msg.linear.x = speed
        speed_pub.publish(vel_msg)
        rate.sleep()
        #twist.angular.z = 2.0
        
        #distance = distance+abs(0.5*math.sqrt(((x_coord-x_ini) ** 2) + ((y_coord-y_ini) ** 2)))
        distance = math.sqrt(((x_coord-x_ini) ** 2) + ((y_coord-y_ini) ** 2))
        
        rospy.loginfo("[Publishing] distance travelled = "+str(distance))



        if(distance>=goal_distance):
            #Final stepp vvimp set velocity back to zero
            vel_msg.linear.x = speed
            speed_pub.publish(vel_msg)
            rospy.loginfo("Goal Reached !")
            break


if __name__ == '__main__':
    try:

        rospy.init_node('move_turtle', anonymous=True)

        #initialize the speedpublisher node
        speed_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, pose_callback) 
        time.sleep(2)
        dis = input('Enter distance')
        spe = input('Enter speed')

        move_turtle(dis,spe)

        print 'start reset: '
        rospy.wait_for_service('reset')
        reset_turtle = rospy.ServiceProxy('reset', Empty)
        reset_turtle()
        print 'end reset: '
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
