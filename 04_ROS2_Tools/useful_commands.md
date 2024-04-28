## Launch an executable
### Launching the executable from ros2 global installation folder or ros2 workspace. For example, let's launch a executable(e.g, "talker") from a global package(e.g, demo_nodes_cpp). 
```bash
ros2 run demo_nodes_cpp talker 
```
# _______________________________________________________________________________________________________________________________________
## help message for the command
```bash
ros2 run -h
```
# _______________________________________________________________________________________________________________________________________
## Enquiring current running nodes
```bash
ros2 node list
```
# _______________________________________________________________________________________________________________________________________
## Get information about running nodes
### please note that the node should be launched before. 
```bash
ros2 node info /<node_name>
```
# _______________________________________________________________________________________________________________________________________
## To get to know Data(Message) type there is a command:
```bash
ros2 interface show example_interfaces/msg/String
```
### the following message will appear on screen which gives us many infos about message type, esp. the last line "string data"
```bash
# This is an example message of using a primitive datatype, string.
# If you want to test with this that's fine, but if you are deploying
# it into a system you should create a semantically meaningful message type.
# If you want to embed it in another message, use the primitive data type instead.
string data
```
