#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node): 
    def __init__(self):
        #in the following we will call the parent's class (Node) constructor, which ensures that the parent's attributes (name) are initialized before ...
        # ... the child adds it's own server or get_logger()
        
        # the name of the name is being specified as follows    
        super().__init__("add_two_ints_server")
        
        # in the following we will create a service from the node object. 
        # we will give it 1- a type,"AddTwoInts"
        #                 2- a name, "add_two_ints" (this is the name of the service)
        #                 3- a callback, "callback_add_two_ints"
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add two ints server has been started.")


    # Write a callback function, as a convention I can write "callback"+the name of the service e.g. here "add_two_ints"
    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum) )
        return response 

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
