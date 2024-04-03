# install a node
## how to install a node in ROS2. For running the nodes, we can just use the following command to create a executable:
```bash
chmod +x my_first_node_oop.py
```
### then run the file as below:
```bash
my_first_node_oop.py
```
## If we always want to run our node, from the terminal directly like above, it's not that scalable.
## We will be able to have much more functionalities, if we sort the file and do the following steps. 

## In ROS2 we can install the node somewhere and call it which is beneficial.
# setup.py & setup.cfg
## setup.cfg file will tell you where to install the python files as below:
```text
[develop]
script-dir=$base/lib/my_py_pkg
[install]
install-scripts=$base/lib/my_py_pkg
```
