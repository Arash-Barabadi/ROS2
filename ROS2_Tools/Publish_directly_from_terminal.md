## you can also publish directly from the terminal,
### usually you use "ros2 topic echo /'topic_name' " command,
```bash
ros2 topic echo /robot_news 
```
###  but still it's good to know the following command line;

```bash
ros2 topic pub -r 10 /robot_news  example_interfaces/msg/String "{data: 'Hello from terminal'}"
```

### As can be seen we have two publishers and one subscriber. 
