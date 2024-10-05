## When we are using external packages, like "example_interfaces", we need to write our program dependency on them as follows:

### 1- package.xml
```xml
  <depend>example_interfaces</depend>
```
### 2- CMakeLists.txt
```txt
find_package(example_interfaces REQUIRED)
```

# How to run the a %%%.cpp code?
## to run a code, we first to need compile it. So
### 1- first we need to build an executalbe as below:
```txt
add_executable(robot_news_station src/robot_news_station.cpp)
ament_target_dependencies(robot_news_station rclcpp example_interfaces)
```
#### on above we are saying that the robot_news_station executable needs both "rclcpp" and "example_interfaces" libraries.
