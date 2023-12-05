### If you have a sensor in your robot and want to use this type in different places. So you have one executable which can be used in diffrent applications simultaneously. For avoiding typing the same code many times, use the following command;
```bash
ros2 run "package_name" "node_name" --ros-args --remap __node:="new_node_name"
```
### Therefore we can use 1 executable for manay nodes. 
