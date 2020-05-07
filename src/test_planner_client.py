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
    obs = obstacles
    num = (goal_y - point_y)
    den = (goal_x - point_x)
    blocked = False
    waypoints = goal
    if den == 0:
        x = point_x
        for y in range(int(point_y), goal_y):
            if distance((x, y), obs) <= 3:
                # obs_ avoidance
                blocked = True
                return blocked, obs
    else:
        for x in range(int(point_x), goal_x):
            slope = (goal_y - point_y) / (goal_x - point_x)
            print(slope)
            b = point_y - point_x * slope
            y = slope * x + b
            if distance((x, y), obs) <= 3:
                # obs_ avoidance
                blocked = True
                return blocked, obs

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
        self.obs_subscriber = rospy.Subscriber('/obs_turtle1/pose', Pose, self.update_obs)
        self.pose = Pose()
        self.rate = rospy.Rate(1)

    def update_obs(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        self.rate.sleep()


if __name__ == '__main__':
    rospy.init_node('Planner', anonymous=True)
    goal_client(1, 1)
    obs = obstacle()
    turtle = TurtleBot()
    while not rospy.is_shutdown():
        init_pose = (turtle.pose.x, turtle.pose.y)
        goal = (6, 8)
        obs_t = (obs.pose.x, obs.pose.y)
        print(obs_t)
        if obs.pose.x != 0:
            blocked, point = line_of_sight(init_pose, goal, obs_t)
            if blocked:
                print('blocked. obstacle at:', point)
                print('rerouting')
                stillblocked, point = line_of_sight(
                    init_pose, (init_pose[0], goal[1]), obs_t)
                waypoints = [(init_pose[0], goal[1]),goal]
                print('new waypoints:', waypoints)
                if not stillblocked:
                    for waypoint in waypoints:
                        goal_client(waypoint[0],waypoint[1])
                        print(going)
                    stillblocked = True
            else:
                print('clear. Going to goal at:', point)
                goal_client(goal[0],goal[1])
        else:
            print('No obstacles. Going to goal at:', goal)
            goal_client(goal[0],goal[1])
        rospy.sleep(1)
