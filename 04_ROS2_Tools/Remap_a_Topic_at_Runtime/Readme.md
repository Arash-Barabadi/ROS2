# Remap a topic
## Remapping a topic is quite useful in your application. For example, when you have an exisiting(running) publisher and you can't change the topic name. Then, remapping a topic is the solution. 
## For example, the publisher is : robot_news_station, the subscriber is : smartphone and the topic is: /robot_news
## Now If I want to change the robot_news name I will write the following line:
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r robot_news:=my_news
```
## then the publisher is called, now I call the subscriber, but nothing appear on terminal. The reason is that as the image below.
![Screenshot from 2024-04-29 21-15-53](https://github.com/Arash-Barabadi/ROS2/assets/54539090/355a30d2-71bb-4538-a2c6-063275b89fce)
