## ROS 2 nodes use the following methods for communication:

#    Topics:
## Nodes communicate by publishing messages to topics or subscribing to topics to receive messages. Topics are generally used for continuous or streaming data like sensor readings. Nodes discover each other over the network and automatically establish a connection without manual intervention.
#    Services: 
## A service in ROS 2 is a synchronous request-response communication model where one node acts as a client and another as a server. This model is suitable for command-based interactions, like asking a robot to move to a specific location.
#    Actions: 
## Actions are designed for tasks that may take some time to complete and can benefit from periodic feedback or can be canceled if necessary. For example, moving a robot arm to a position would be a task that benefits from feedback and may need cancellation if conditions change.
___________________________________________________________________________________
# Topic
## A topic is a named bus over which nodes exchange messages.
### 1. Data stream is unidirectional. Some nodes can publish to a topic, and some nodes can subscribe to a topic. However, there is no response from a subscriber to a publisher. The data is only flowing in one direction.
### 2. As mentioned above, a node (either publisher or subscriber) isn't aware of another node's existence. Therefore, publishers and subscribers are anonymous. A publisher only knows it is publishing to a topic, and a subscriber only knows it is subscribing to a topic.
### 3. A topic has a message type. All publishers and subscribers to a topic must use the same message type associated with that topic.
### 4. A node can have many publishers/subscribers for many different topics.
# ___________________


