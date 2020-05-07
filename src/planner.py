#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from plannersrv import *

waypoints = [(1,1),(1,8),(8,8)(8,1)]

def goal_client(waypoints)
	rospy.wait_for_service('moveto_goal')
	try:
		for waypoint in waypoints:
		MoveTo = rospy.ServiceProxy('moveto_goal',MoveTo)
		MoveTo(waypoint)
	except rospy.ServiceException, e:
		print('service call failed')

if __name__ == '__main__':
	waypoints = [(1,1),(1,8),(8,8)(8,1)]
	goal_client(waypoints)