#!/usr/bin/env python
from __future__ import division

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import math as m
from learning_tf.srv import *


def distance(path, obs):
    return m.sqrt((obs[0] - path[0])**2 + (obs[1] - path[1])**2)


class TurtleBot:
    def __init__(self):
        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)


def line_of_sight(point, goal, obstacles):
    goal_x = goal[0]
    goal_y = goal[1]
    point_x = point[0]
    point_y = point[1]
    num = (goal_y - point_y)
    den = (goal_x - point_x)
    if den == 0:
        x = point_x
        for y in range(point_y, goal_y):
            if distance((x, y), obs) <= 2:
                # obs_ avoidance
                blocked = True
                return blocked, obs
            else:
                waypoints = goal
                blocked = False

    else:
        for x in range(point_x, goal_x):
            slope = (goal_y - point_y) / (goal_x - point_x)
            print(slope)
            b = point_y - point_x * slope
            y = slope * x + b

            print("loc", x, y)
            if distance((x, y), obs) <= 2:
                # obs_ avoidance
                blocked = True
                return blocked, obs
            else:
                waypoints = goal
                blocked = False
    return blocked, waypoints


def goal_client(x, y):
    rospy.wait_for_service('turtle_controller')
    try:
        MoveTo = rospy.ServiceProxy('turtle_controller', turtle_msg)
        MoveTo(x, y)
        print('Waypoint Reached')
    except rospy.ServiceException:
        print('service call failed')


class obstacle():
    def __init__(self):
        obs_subscriber = rospy.Subscriber('/obs_turtle1/pose', Pose, self.update_obs)
        rospy.spin()
        print(obs_subscriber)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_obs(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        print('updated obs')

if __name__ == '__main__':
    rospy.init_node('Planner', anonymous=True)
    obs = obstacle()
    print(obs.pose)
    init_pose = (1, 1)
    goal = (6, 8)
    obs = (5, 7)
    turtle = TurtleBot()
    print(turtle.pose)
    rospy.spin()
    blocked, point = line_of_sight(init_pose, goal, obs)
    if blocked:
        print('blocked. obstacle at:', point)
        print('rerouting')
        stillblocked, point = line_of_sight(
            init_pose, (init_pose[0], goal[1]), obs)
        print(stillblocked, point)
    else:
        print('clear. Going to goal at:', point)
    rospy.spin()

