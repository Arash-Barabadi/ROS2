# Creation of Publisher
##
##

## You can also publish directly on the terminal, without calling any node. 
### Publishment at 10 Hz on a topic with arbitrary name "/arbitrary".
```bash
ros2 topic pub -r 10 /arbitrary example_interfaces/msg/String "{data: 'hello from terminal'}" 
```
## without typing any command to activate the node or writing any program to produce the publisher, we have activated the Publisher through just 1 command line. 
## To check whether it is activated, type in the following command. 
```bash
ros2 topic list
```
### and the outputs were :
```bash
/arbitrary
/parameter_events
/rosout
```
### as can be seen above /arbitrary is on the list of topics.

## and if you check whether any node relating to the publisher was existed, type in the following command. 
```bash
ros2 node list
```
### and it shows us nothing. because we haven't acitvated any nodes.
