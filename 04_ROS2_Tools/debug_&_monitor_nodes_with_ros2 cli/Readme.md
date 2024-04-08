## Launch an executable
### Launching the executable from ros2 global installation folder or ros2 workspace. For example, let's launch a executable(e.g, "talker") from a global package(e.g, demo_nodes_cpp). 
```bash
ros2 run demo_nodes_cpp talker 
```
## help message for the command
```bash
ros2 run -h
```
## Enquiring current running nodes
```bash
ros2 node list
```
## Get information about running nodes
### please note that the node should be launched before. 
```bash
ros2 node info <node_name>
```
