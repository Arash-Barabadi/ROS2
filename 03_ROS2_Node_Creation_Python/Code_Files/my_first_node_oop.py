#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Generate a class from the above imported Node object.
class MyNode(Node):
    # then we wright the constructor of the class
    def __init__(self): 
        # the below __init__ funtion called from the Node which is imported. 
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(1, self.timer_callback)
        


# Timer will allow you to call the function at a given rate. 
#For example, you want to call a function at 10Hz then timer comes into play.
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):

    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" : 
    main()
