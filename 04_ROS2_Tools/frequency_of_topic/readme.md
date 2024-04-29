# Publishing Frequency
## If you want to know the frequency at which the data is published, the following command will be helpful:
```bash
ros2 topic hz /robot_news
```
### This command can be great for debugging. For example, if you have a very high pulish rate and you see the messages are not flowing quickly enough, maybe the rate has dropped. Then you can check it by the above command.
### It prints the average rate 1.99, which is right. As we defined already in publisher file. 
```bash
average rate: 1.999
	min: 0.500s max: 0.500s std dev: 0.00013s window: 3
```
# Band width
## You can see the Bandwidth used for the node. 
```bash
ros2 topic bw /robot_news
```
### and the following message sequentially appears on the console:
```bash
Subscribed to [/robot_news]
145 B/s from 2 messages
	Message size mean: 56 B min: 56 B max: 56 B
```

