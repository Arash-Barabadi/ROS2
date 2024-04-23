# Hints
## Publishing principals

## As we want to publish a "string" to a topic, the data type or message type should be of a "String" type.
### in bash, we will write the following line to check that whether data type "String" is excited in a package called "example_interfaces", and if that is the right choice we will take it.
```bash
ros2 interface show example_interfaces/msg/String
```
### accordingly, the following text appears:
```bash
# This is an example message of using a primitive datatype, string.
# If you want to test with this that's fine, but if you are deploying
# it into a system you should create a semantically meaningful message type.
# If you want to embed it in another message, use the primitive data type instead.
string data
```
#### string  is a primitive data type for ROS2 messages.
#### data  is a name of the field.

# Message type
## When we want to use a message type that has been deployed in another package(e.g., we should mention that package in our python publisher as well as in our package.xml files. 
### in publisher we will type in:
#### the term "String" is a desired message type.
```python
from example_interfaces.msg import String
```
### and in package.xml we will type in the package name:
#### every time your package depends on another package, write that like the below line.  
```xml
<depend>example_interfaces</depend>
```
### as can be seen from below ...
```python
self.publisher_ = self.create_publisher(String,"robot_news", 10)
```
#### we have created a publisher with ...
##### data type "String"
##### and a topic name of "robot_news"
##### a queue size 10, disctiption: when you publish or when you subscribe, we need to give that argument. You will send some messages between nodes and sometimes it can happen if you publish very fast or if you publish a big messages like a complete image. It can happen that some messages are late to arrive and in that case the queue size will allow you to keep some messages before they are processed. 

