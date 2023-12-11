
## Rename a Node:
### If you have a sensor in your robot and want to use this type in different places. So you have one executable which can be used in diffrent applications simultaneously. For avoiding typing the same code many times, use the following command;
```bash
ros2 run "package_name" "node_name" --ros-args --remap __node:="new_node_name"
```
## or
```bash
ros2 run "package_name" "node_name" --ros-args -r __node:="new_node_name"
```
### For instance;
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station
```
### Therefore we can use 1 executable for many nodes.
## __________________________________________________________________________
## Rename a Topic
### for the Publisher
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r robot_news:=my_news
```
### or if you want rename both node and topic name, therefore;
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=my_news
```
### for the Subscriber
```bash
ros2 run my_py_pkg smartphone --ros-args -r robot_news:=my_news
```
