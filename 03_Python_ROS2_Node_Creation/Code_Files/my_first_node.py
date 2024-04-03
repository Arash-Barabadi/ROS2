#!/usr/bin/env python3

# on above the interpreter line for Python is written. ROS2 works only with python3, no python2 anymore. 

# To use ROS2 functionalities we will type in ...
import rclpy

# Import the Node class
from rclpy.node import Node

##in the following we create a main function here. 
## for now we will put optional Argument here.

def main(args=None):
#__1__ We initialize ROS2 communication 
    rclpy.init(args=args)

# __2__ We will add a node inside the main, so we'll create a node, 
# and to do that we have imported Node class on the initial lines of the code.

# The name of the Node (here : py_test) is not the name of the file (which is "my_first_node.py")
    node = Node("py_test")

# __3__ As desired, the node should do something. Here we will only output a message.
    node.get_logger().info("Hello ROS2")

# __4__ Spin will basically allow our node to continue to be alive,but the program (my_first_node.py) is paused at this point
# The callback in future will be able to called from spin() function
    rclpy.spin(node)

# __5__ We shutdown ROS2 communication
    rclpy.shutdown()

# We will create a structure for the main.
if __name__ == "__main__" : 
    main()

    