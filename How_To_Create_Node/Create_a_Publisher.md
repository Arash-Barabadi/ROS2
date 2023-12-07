# Creation of Publisher
##
##

## You can also publish directly on the terminal. 
### Publishment at 10 Hz
```bash
ros2 topic pub -r 10 /robot_news example_interfaces/msg/String "{data: 'hello from terminal'}" 
```
## without typing any command to activate the node, we have actiated the Publisher. to check whether it is activated, type in the following command. 
```bash
ros2 topic list
```
### and the outputs were :
/parameter_events
/robot_news
/rosout
### as can be seen in above "/robot_news" is activated, which is a publisher. 
