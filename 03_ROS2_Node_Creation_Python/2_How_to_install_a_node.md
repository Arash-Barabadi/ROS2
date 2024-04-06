# install a node
## how to install a node in ROS2. there are 3 ways to do that. 
# 1- For running the nodes, we can just use the following command to create a executable:
```bash
chmod +x my_first_node_oop.py
```
### then run the file as below:
```bash
./my_first_node_oop.py
```
## If we always want to run our node, from the terminal directly like above, it's not that scalable.
## We will be able to have much more functionalities, if we sort the file and do the following steps. 

## In ROS2 we can install the node somewhere and call it which is beneficial.
# 2- setup.py & setup.cfg
## setup.cfg file will tell you where to install the python files as below:
```text
[develop]
script-dir=$base/lib/my_py_pkg
[install]
install-scripts=$base/lib/my_py_pkg
```
## setup.py has 2 functionalities.
## A- to put your info, when you want to release the software.
```python
from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arash',
    maintainer_email='arash.barabadi@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
#        'console_scripts': [
#            "py_node = my_py_pkg.my_first_node:main"
#        ],
#    },
)
```
### So if you take a look at this setup.py file, you have version,maintainer, description, license. And that is quite similar to what we had in the package.xml. So if you need to release the package, you have to change the info in both of these two files.

## B- to install the node you want to compile.
### to install a node, we will add a new line here and we will need to specify a name for the executable.So what will ROS2 do when we install the file? It will copy the python file (for example my_first_node.py) then make some modification so it becomes an executable.And that exevutable, will be installed in the "install folder" of ROS2 workspace. 
### So we need to specify a name for the executable. Again refering to python.py we have :....
```python
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main"
# py_node : executable name
        ]
```
### then go back to the terminal and write down the following line:
```bash
~/ros2_ws$ colcon build --packages-select my_py_pkg
```
### let's see where this node has been installed. As mentioned in setup.cfg :
```bash
~/ros2_ws/install/my_py_pkg/lib/my_py_pkg
```
### Note : before executing ./py_node run "source ~/.bashrc" because this will source your ROS2 workspace for the bash environment. When you create a new package or a new node, it's always better to source your environment through the bash. 
```bash
~/ros2_ws/install/my_py_pkg/lib/my_py_pkg$ source ~/.bashrc
~/ros2_ws/install/my_py_pkg/lib/my_py_pkg$ ./py_node 
```
### in it works.
# 3- the third and the best way. After installing the node, through the above steps, then type in the terminal (No matter if it's in main directory or not:). Please note that py_node is the executable name.
```bash
ros2 run my_py_pkg py_node 
```


