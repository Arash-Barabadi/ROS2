## For example, if you have a node for a temperature sensor and if you have 5 temperature sensors, then you'll want to launch a same node five times and of course with a different name for each sensor, because if you launch the same node with the same name more than 1 time, this can have unintended side effects. 
## The solution for that is to rename the same node, as many time as you need. we call it REMAPping as follows:
### Please note that in the following we'll write the executable name after pacakge name, but after __node:=  we'll write new node name. 
```bash
ros2 run <package_name> <executable_name> --ros-args --remap __node:=<new_node_name>
```
## or
```bash
ros2 run <package_name> <executable_name> --ros-args -r __node:=<new_node_name>
```
### For instance;
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station
