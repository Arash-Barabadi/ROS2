# ROS2
## COLCON
### to create your own ROS2 programs, you will need a build tool specific to ROS2. So this build tool is called colcon and is created specifically for the ROS2. 
### The installation procedure of colcon is as follows: 
```bash
sudo apt install python3-colcon-common-extensions
```
### The colcon is now installed and can be used. There is one more thing which needs to be set up with Colcon, that is the auto completion feature.
### The auto completion feature is not enabled by deafualt, so we will active that as follows... 
### at first go to the following location
```bash
cd /usr/share/colcon_argcomplete/hook/
```
### there the colcon_argcomplete.bash is availabe. Then we can source it in .bashrc file as follows: ...
```bash
gedit ~/.bashrc
!then copy-paste the colcon_argcomplete.bash file address and save the changes.
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```
## Workspace
### This workspace will be the place where you write all your codes for a ROS2 application. And that's also where you will compile these codes.
### Workspace creation
#### Let's first go to the home directory and create a folder named ros2_ws. The name of the folder is arbitrary. But this is the convention which can be seen in ros2 community, which is to name the workspace like : name.ws
```bash
mkdir ros2_ws
```
#### inside this folder we are going to create a src folder, which is source folder. All the code and packages we are going to create later will be in the source folder of that workspace.
```bash
cd ros2_ws
mkdir src
```
### So now go to the ros2_ws folder directory, then by typing "colcon build", the actual workspace will be built.
### pay attention that we should be at the ros2_ws directory then type the following command. 
```bash
colcon build
```
### Now, if I check the contents, there are three folders next to the 'src' directory
#### log : which contains log of the build process.
#### build : 
#### install : 
### In the installation folder, you will find a 'setup.bash' script as well as a 'local_setup.bash' script.
### So if I want to use whatever I've created in this workspace, I have to source local_setup.bash script. 

#### We have a "local_setup.bash" and a "setup.bash" files. What is the difference?
#### "local_setup.bash" simply sources the workspace ros2_ws (Overlay Workspace). When using the "local_setup.bash" script, I can access everything I've created in the ros2_ws workspace. 
#### "setup.bash" will source the ros2_ws (overlay) and the global ROS2 installation (underlay workspace). For simplicity, the following command should be written into the .bashrc file to use the "setup.bash".
