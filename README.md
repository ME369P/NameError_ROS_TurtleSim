# TurtleSim

## Packages used:
TurtleSim

## Goal:
This project aims to integrate a basic path planning algorithm to set waypoints and avoid obstacles in the basic ROS TurtleSim package. It demonstrates and expands on the basic concepts of ROS and path planning a robot in a simulated environment.

## Using the Code:
Clone this repository into a catkin workspace on your computer and run the .launch files through the terminal depending on which demo you want to run. It is also possible to download the source code for ROS TurtleSim from the official GitHub, modify the source code in C++, and use the modified package instead of the preinstalled ROS TurtleSim package. To do this, clone the repository to a catkin workspace:
https://github.com/ros/ros_tutorials

Our demos include:
- Spawning a second turtle into the map as an "obstacle"
- Drawing a square using waypoints
- Adding basic path planning around an obstacle in the turtle's path

## Future Applications:
This project can potentially be recreated by programming a similar path planning algorithm in Gazebo, a ROS simulation tool. We have already taken some steps toward this goal, including:

- Incorporated depth camera sensor into turtlebot by adding plugins to the code
- Manipulated turtlebot 3 to move with live commands

### Next Steps for this Project:
- Using the depth camera on the bot to create a map of the environment
- Localizing the robot
- A package will contain files related to localization (a launch file will launch the node and add the necessary parameters in order to properly configure it)
- Incorporate the path planning system
- Use a ROS program to interact with the nav stack

# Resources:
The original tutorial for moving the turtle from Point A to Point B can be found here: http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal

We also adapted the listener and broadcaster nodes from these ROS tutorials:
http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29
http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29

# Path Planning Algorithm:
The path planning algorithm is included in the line_of_sight function in our test_planner_client.py file in the src folder.

The line-of-sight obstacle avoidance works by getting the equation of a line and stepping through x positions to see if there is an obstacle within a radius of the turtle's path. If there is an obstacle identified, the turtle can "sidestep" the obstacle by taking a different path. The following diagram offers a simple illustration of this concept.

![Obstacle Avoidance](https://github.com/noelbrownback/TurtleSim/blob/master/obstacle_avoidance.png)




