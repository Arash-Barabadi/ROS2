# Package
## To create a ROS2 node, firstly you need a package.
## Packages will allow you to separate your code into reusable blocks.
## Each package is an independent unit, for example, you can have one package that will handle a camera, another package for the wheels of the robot, and yet another package that will hanlde the motion planning for the robot in the environment. 
## So, let's create a python package in the new ROS2 workspace. 
## At first you will navigate to the source directory of your workspace. 
```bash
cd ~/ros2_ws/src
```
## And to create a new package you simply type ...
```bash
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```
## we now have a folder named my_py_pkg. LEt's see what wee got in this folder(my_py_pkg)
### my_py_pkg: 1st folder was generated with the same name of the package(my_py_pkg). In this folder one must put all nodes of the package. It already contains __init__.py file. (I will talk about this python file later. But now it's not necessary to open it.) 
### resource folder: which doesn't need to be opened now. 
### test folder: which already contains 3 test files. All the test files should be located here. 
###
