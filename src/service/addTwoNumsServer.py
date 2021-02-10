#!/usr/bin/env python

from ros_basics.srv import addTwoNums
from ros_basics.srv import addTwoNumsRequest
from ros_basics.srv import addTwoNumsResponse

import rospy

def handleAddTwoNums(req):
    print("Returning "+str(req.x)+"+"+str(req.y)+"="+str(req.x+req.y))
    return addTwoNumsResponse(req.x+req.y)

def addTwoNumsServer():
    rospy.init_node('addTwoNumsServer')
    s= rospy.Service('addTwoNums',addTwoNums,handleAddTwoNums)
    print("Ready to add two numbers")
    rospy.spin()

if __name__ == "__main__":
    addTwoNumsServer()