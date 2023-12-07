# Creation of Publisher
##
##

## You can also publish directly on the terminal. 
### Publishment at 10 Hz
```bash
ros2 topic pub -r 10 /robot_news example_interfaces/msg/String "{data: 'hello from terminal'}" 
```
