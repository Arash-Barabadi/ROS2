### If you want to update your package repeatedly without typing colcon build (compile the file) every time in terminal window. first got to your workspace folder then use the below command;
```bash
colcon build --packages-select "package_name" --symlink-install
```
#### !! beforehand make sure your python file (node) is set as an executalb with the following command line. 
```bash
chmod +x my_first_node.py
```
