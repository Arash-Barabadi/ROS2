# Publish ditrectly from the terminal
## Usually we use ros2 topic echo </topic_name> command, but if you want to change what the message is, then used the following command. 
### ros2 topic pub -r 10 <frequency> /robot_news example_interfaces/msg/String <data_type>  "{data: 'Hey jude'}" <Message>
```bash
ros2 topic pub -r 10 /robot_news example_interfaces/msg/String "{data: 'Hey jude'}"
```
