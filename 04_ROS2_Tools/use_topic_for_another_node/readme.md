## Whenever you want to use the topic that has been created before. Just run the node either Publisher or Subscriber. So : 
```bash
ros2 run my_py_pkg <package_name> robot_news_station <executable_name>
```
## Now if you enguire the topic list you can find the topic which relates to the above running node.
```bash
ros2 run <Package_name> <Node_name>
```
## Now take the name of the topic and use it as follows;
```bash
ros2 topic info /robot_news </Topic_Name>
```
## Then the messages like the below would come up on screen:
```bash
arash@arash-HP-ZBook-15-G2:~$ ros2 topic info /robot_news 
Type: example_interfaces/msg/String
Publisher count: 1
Subscription count: 0
```
