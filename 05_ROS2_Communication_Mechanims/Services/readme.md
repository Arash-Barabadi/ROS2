#    Services: 
## A service in ROS 2 is a request-response communication model where one node acts as a client and another as a server. This model is suitable for command-based interactions, like asking a robot to move to a specific location.
### 1. A ROS2 Service is a client/server system.
### 2. It can be either synchronous or asynchronous. 
### 3. A Service is defined as a name and a pair of messages (One message type for Request, One message type for Response)
### 4. A Service server can only exist once, but can have many clients. 
### 5. You can see that services offer a nice complementarity with topics. Topics will be used for unidirectional data streams and services will be used for bidirectional and when you need a client server architecture. 

## We will create a service server in python that will take two numbers as a request and return the sum as a response.
## So let's use the service definition here and in the above folder we created our own service definition. 
```bash
arash@arash-HP-ZBook-15-G2:~/ros2_ws/src/my_py_pkg/my_py_pkg$ touch add_two_ints_server.py
```
## then we make it executable
```bash
arash@arash-HP-ZBook-15-G2:~/ros2_ws/src/my_py_pkg/my_py_pkg$ chmod +x add_two_ints_server.py 
```
