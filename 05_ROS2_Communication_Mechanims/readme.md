## ROS 2 nodes use the following methods for communication:

#    Topics:
## Nodes communicate by publishing messages to topics or subscribing to topics to receive messages. Topics are generally used for continuous or streaming data like sensor readings. Nodes discover each other over the network and automatically establish a connection without manual intervention.
#    Services: 
## A service in ROS 2 is a synchronous request-response communication model where one node acts as a client and another as a server. This model is suitable for command-based interactions, like asking a robot to move to a specific location.

#    Actions: 
## Actions are designed for tasks that may take some time to complete and can benefit from periodic feedback or can be canceled if necessary. For example, moving a robot arm to a position would be a task that benefits from feedback and may need cancellation if conditions change.




