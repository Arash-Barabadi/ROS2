### If you want to update your package repeatedly without typing colcon build (compile the whole workspace) every time in terminal window. first got to your workspace folder then use the below command;
```bash
colcon build --packages-select <package_name>
```
## So everytime youu modify your files, in one package, you will have to build it again. Unless you --simlink-install argument. Therefore, you don't need to compile the file again, and modify your python (not c++) file as you wish without compling every time. 
```bash
colcon build --packages-select <package_name> --symlink-install
```
### Please not that the python file must be executable. to make it executable, do the following.
```bash
~/ros2_ws/src/my_py_pkg/my_py_pkg$ chmod +x my_first_node.py
```
