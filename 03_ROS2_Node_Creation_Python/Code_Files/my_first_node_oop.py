#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Generate a class from the above imported Node object.
class MyNode(Node):
    # then we wright the constructure of the class
    def __init__(self): 
        # the below __init__ funtion called from the Node which is imported. 
        super().__init__("py_test")
        self.get_logger().info("Hello ROS2")



def main(args=None):

    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" : 
    main()
 
    