# Hints
## Mesaage type, topic name, queue size ...
## As we want to publish a "string" to a topic, the data type or message type should be of a "String" type.
### in bash, we will write the following line to check the data type "String", and if that is the right choice we will take it.
```bash
ros2 interface show example_interfaces/msg/String
```
### accordingly, the following text appears:
```bash
# This is an example message of using a primitive datatype, string.
# If you want to test with this that's fine, but if you are deploying
# it into a system you should create a semantically meaningful message type.
# If you want to embed it in another message, use the primitive data type instead.
string data
```


```python

