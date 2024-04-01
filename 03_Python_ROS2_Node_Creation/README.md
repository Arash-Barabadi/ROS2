# Ros2 Node
## What is a ROS2 node? A Node is a subpart of your application and should have a single purpose. An application will contain many nodes which will be put into packages.These nodes will communicate with each other.
## Nodes are combined into graph and communicate between each other using ROS topics, service and parameters. 
## What are the characteristics and benefits of nodes: 
## Benefits: 
### 1- Reduce code complexity: If one correctly seprate the application into packages and nodes, then it will be much easier to scale the application. If you write everything in one block, then after some time you'll spend more time fixing your code than actually developing new functionalities. 
### 2- Nodes also provide a greate fault tolerance. If you run your nodes in different processes, then they are not directly linked and they can still continue to communicate. So if one node crashes, it will not make the other nodes crash. First : That's good for debugging. Second, that's great if you have a critical node running your hardware that is well tested and you just add another new node in your program, even if this later node can crash, it will not affect the critical hardware node. 
### 3- ROS2 is language agnostic. It means you can write one node in python, another node in C++ and both nodes can communicate without any problem. This characteristic is really great. For example, you can choose to develope your entire application in python while some nodes, as they need fast execution speed, written in C++.
