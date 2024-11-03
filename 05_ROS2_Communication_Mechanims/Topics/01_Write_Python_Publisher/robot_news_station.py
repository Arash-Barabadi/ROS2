#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

### Constructor begine ####
#_____________________________________________________________________________________________
class RobotNewsStationNode(Node): 
    def __init__(self):
        # we are going to create and start the node
        super().__init__("robot_news_station")

        # We create a name for the robot
        self.robot_name_ = "C3PO"
        # Inside the node we will create a publisher
        self.publisher_ = self.create_publisher(String,"robot_news", 10)
        
        # Then we will create a timer which call the function "publish_news" at 2 Hz.
        self.timer_ = self.create_timer(0.5, self.publish_news)

        # Then for the purpose of the DEBUGGING, we print something as below.
        self.get_logger().info("Robot News Station has been started.")
    # Now we will create a function to publish on this "robot_news" topic.

    def publish_news(self): 
        msg = String()
        msg.data = "Hi, this is "+ str(self.robot_name_)+ " from the robot news station."
        self.publisher_.publish(msg)
    
#____________________________________________________________________________________________
### Contructor exit ###

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()