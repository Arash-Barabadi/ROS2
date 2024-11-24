#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

def main(args=None):
    
    #rclpy.init(): Initializes the ROS2 Python client library.
    rclpy.init(args=args)
    
    # Node("add_two_ints_no_oop"): Creates a node named "add_two_ints_no_oop". 
    #The node serves as the interface to ROS 2 and handles communication.
    node = Node("add_two_ints_no_oop")


    # the following creates a client for the service named "add_two_ints".
    client = node.create_client(AddTwoInts, "add_two_ints")
    
    # We will check if the service server (add_two_ints) is available.
    # If the server is not ready, it logs a warning every 1.0 seconds.
    # This ensures the client does not proceed until the server is available.
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for Server Add two Ints...")
    
    
    # the following creates a request object with fields a and b (the integers to be added).
    request =AddTwoInts.Request()
    request.a = 3
    request.b = 8
    
    #Calling ....
    # Making an Asynchronous Call
    # Sends the service request asynchronously. It does not block the program.
    # Returns a Future object that will hold the result of the service call once it is complete.
    future = client.call_async(request)
    
    # The following command Blocks execution and processes ROS 2 events until the future is complete (i.e., the server sends a response).
    rclpy.spin_until_future_complete(node, future)
    
    
    # the following retrieves the result of the service call.
    # In this case, it contains the sum field, which is the sum of a and b.
    
    try:
        response = future.result()
        node.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
    except Exception as e:
        # If the service call fails, logs an error message with the exception details.
        node.get_logger().error("Service call failed.%r" % (e,))
    
    
    #Shuts down the ROS 2 client library and cleans up resources.
    rclpy.shutdown()


if __name__ == "__main__":
    main()
    
