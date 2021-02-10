#!/usr/bin/env python

import sys
from ros_basics.srv import addTwoNums
from ros_basics.srv import addTwoNumsRequest
from ros_basics.srv import addTwoNumsResponse

import rospy


def addTwoNumsClient(x,y):
    rospy.wait_for_service('addTwoNums')
    try:
        add_Two_Nums = rospy.ServiceProxy('addTwoNums',addTwoNums)
        resp1 = add_Two_Nums(x,y)
        return resp1.sum
    except rospy.ServiceException, e:
        print("Service call Failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv)==3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print("Requesting %s+%s"%(x,y))
    print("%s+%s=%s"%(x,y,addTwoNumsClient(x,y)))
