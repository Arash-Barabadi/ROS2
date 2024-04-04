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
## setup.py has 2 functionalities.
## 1- to put your info, when you want to release the software.
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

## 2- to install the node you want to compile.
### to install a node.
