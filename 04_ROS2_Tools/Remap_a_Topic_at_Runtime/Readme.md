# Remap a topic
## Remapping a topic is quite useful in your application. For example, when you have an exisiting(running) publisher and you can't change the topic name. Then, remapping a topic is the solution. 
## For example, the publisher is : robot_news_station, the subscriber is : smartphone and the topic is: /robot_news
## Now If I want to change the robot_news name I will write the following line:
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r robot_news:=my_news
```
## Accordingly the publisher is called, now if the subscriber is called, nothing appears on terminal. As can bee seen from the below image, we have two topics, Publisher publishes to one of them and subscriber subscribes to another one. 
![Screenshot from 2024-04-29 21-15-53](https://github.com/Arash-Barabadi/ROS2/assets/54539090/355a30d2-71bb-4538-a2c6-063275b89fce)
## To combine the both above mentioned topics into one, we should write the following line:
```bash
ros2 run my_py_pkg smartphone --ros-args -r robot_news:=my_news
```
## Now the problem is solved as you can see in the following image. 
![Screenshot from 2024-04-29 21-21-41](https://github.com/Arash-Barabadi/ROS2/assets/54539090/4644e95b-34ad-4466-a063-5579b3352dcf)
