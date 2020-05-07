#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

from learning_tf.srv import *


def goal_client(x,y):
    print('wait')
    rospy.wait_for_service('turtle_controller')
    print('nowait')
    try:
        MoveTo = rospy.ServiceProxy('turtle_controller', turtle_msg)
        print('b')
        finshed = MoveTo(x,y)
        print(finished,'finished')

        # if finished:
        #     next
        # else:
        #     print('failed in moveto')
    except rospy.ServiceException:
        print('service call failed')

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print('request xy:')
    goal_client(x,y)