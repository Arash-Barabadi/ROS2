# Python Service Client
## we will do it in two steps, first without OOP, and then we have an OOP
## we create two files and make them executable afterwards. 
```bash
arash@arash-HP-ZBook-15-G2:~/ros2_ws/src/my_py_pkg/my_py_pkg$ touch add_two_ints_client_no_oop.py
arash@arash-HP-ZBook-15-G2:~/ros2_ws/src/my_py_pkg/my_py_pkg$ touch add_two_ints_client.py
arash@arash-HP-ZBook-15-G2:~/ros2_ws/src/my_py_pkg/my_py_pkg$ chmod +x add_two_ints_client_no_oop.py 
arash@arash-HP-ZBook-15-G2:~/ros2_ws/src/my_py_pkg/my_py_pkg$ chmod +x add_two_ints_client.py
```
# Without OOP

#### --------------------------------------------------------------------------------------------------------------

## How It Works

###    The node add_two_ints_no_oop is started.
###    It creates a client for the add_two_ints service and waits for the corresponding server to be available.
###    When the server is ready, the client sends a request containing two integers (3 and 8).
###    The client waits for the server's response.
###    Once the response is received:
###        If successful, logs the result ("3 + 8 = 11").
###        If an error occurs, logs an error message.
###    Shuts down the node.

### ----------------------------------------------------------------------------------------------------------------


## How It Works

###    The node add_two_ints_no_oop is started.
###    It creates a client for the add_two_ints service and waits for the corresponding server to be available.
###    When the server is ready, the client sends a request containing two integers (3 and 8).
###    The client waits for the server's response.
###    Once the response is received:
###        If successful, logs the result ("3 + 8 = 11").
###        If an error occurs, logs an error message.
###    Shuts down the node.
