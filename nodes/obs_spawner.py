#!/usr/bin/env python
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
roslib.load_manifest('learning_tf')


if __name__ == '__main__':
    rospy.init_node('obs_spanwn')
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5, 7, 0, 'obs_turtle1')
