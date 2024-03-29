# Package
## To create a ROS2 node, firstly you need a package.
## Packages will allow you to separate your code into reusable blocks.
## Each package is an independent unit, for example, you can have one package that will handle a camera, another package for the wheels of the robot, and yet another package that will hanlde motion planning for the robot in the environment. 
## So, let's create a python package in the new ROS2 workspace. 
## At first you will navigate to the source directory of your workspace. 
```bash
cd ~/ros2_ws/src
```
## And to create a new package you simply type ...
```bash
ros2 pkg create
```
