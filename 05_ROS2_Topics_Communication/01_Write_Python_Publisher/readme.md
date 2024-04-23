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
#### string  is a primitive data type for ROS2 messages.
#### data  is a name of the field. 
### It sounds the right choice, so we will take it.
```python
self.publisher_ = self.create_publisher(String,"robot_news", 10)
```
#### String : Data(Message) type
#### "robot_news" : 
#### 10 : queue
