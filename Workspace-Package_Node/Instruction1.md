## Create a Python node inside a Python file
```python
# The interpreter line for python3 as bellow. ROS2 only works with python3 not python2 or older versions.
#!/usr/bin/env python3

#For using ROS2 functionalities, the rclpy library has been imported.
import rclpy
from rclpy.node import Node 


def main(args=None):
    #Initialize the ROS2 communication. 
    rclpy.init(args=args)

    #To construct the node, we should use Node class as an object, and insert the node name as a parameter. 
    #Note that, the name of the node is not the name of the file.
    node = Node("py_test")

    #Please note that, the node is not the executable, the node is inside the executable or the python file. 

    #Let's print something with get_logger. So you will use get_logger function from the node objet.
    node.get_logger().info("Hello ROS2")

    #The following line is used to make your node be alive. The callbacks will be able to be called from spin function.
    rclpy.spin(node)

    #Finish the ROS2 communication.
    rclpy.shutdown()


if __name__ == "__main__" : 
    main()
```
## !! Remeber for the first time of the use of the python file, it should be in terminal written that the python file is executable. Accordingly the following line must be typed :
```bash
chmod +x my_first_node.py

```
## Class
### A template for writing ROS2 python node would be something like below:

```python
#!/usr/bin/env python3

#For using ROS2 functionalities, the rclpy library has been imported.
import rclpy
from rclpy.node import Node 

class MyNode(Node) : 

    def __init__(self):

        #The following line will call __init__ function from the Node objet.
        super().__init__("py_test")
        # instead of node.get_logger() we are gonna use the below line : 
        self.get_logger().info("Hello ROS2")


def main(args=None): 
    #For starting the ROS2 communication the following line must be written. 
    rclpy.init(args=args)

    #To construct the node, we should use Node class as an object, and insert the node name as a parameter. 
    #Note that, the name of the node is not the name of the file. 
    ## node = Node("py_test")  !!instead of creating Node objet. I will create MyNode()
    node = MyNode()

    #Let's print something with get_logger. So you will use get_logger function from the node objet.
    ## node.get_logger().info("Hello ROS2")

    #The following line is used to make your node be alive. The callbacks will be able to be called from spin function.
    rclpy.spin(node)

    #For ending the ROS2 communication the following line must be written.
    rclpy.shutdown()


if __name__ == "__main__" : 
    main()
```
## Timer
### since this node does nothing about printing a log. Let's use one of the most basic and common functionalities in ROS, which is a timer. A timer will allow to call a function with a given rate. A function is needed to be called at 10Hz, for instance, therefore the timer comes into play.

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 

class MyNode(Node) : 

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        #From the Node object we call create_timer function.
        #The first argument is the period between two callbacks (0,5 sec = 2Hz) 
        #The second argument is the function to be called, which is defined inside the class as can be seen ...
        #...below in the def timer_callback(self).  
        self.create_timer(0.5, self.timer_callback)

    #We will add timer directly inside the class
    def timer_callback(self) :
        self.counter_ += 1 
        self.get_logger().info("Hello" + str(self.counter_))

def main(args=None): 
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" : 
    main()
```
## OOP Python Code Template for Nodes
```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 


class MyCustomNode(Node): # Modify the name
    def __init__(self):
        super().__init__("node_name")  # Modify another name here as well
    


def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode() # Modify the Name
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__" : 
    main()
```

