#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

from learning_tf.srv import *


def goal_client(x, y):
    rospy.wait_for_service('turtle_controller')
    try:
        MoveTo = rospy.ServiceProxy('turtle_controller', turtle_msg)
        MoveTo(x, y)
        print('Waypoint Reached')
    except rospy.ServiceException:
        print('service call failed')


if __name__ == '__main__':
    waypoints = [(1, 1), (1, 8), (8, 8), (8, 1),(1,1)]
    for waypoint in waypoints:
        print(waypoint)
        result = goal_client(waypoint[0], waypoint[1])
        if result:
            next
