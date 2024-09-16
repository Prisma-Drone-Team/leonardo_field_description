# Leonardo field description with Ros2 and Gazebo Garden

```sh
mkdir -p your_folder/ros2_ws/src
cd your_folder/ros2_ws/src
git clone https://github.com/Prisma-Drone-Team/leonardo_field_description.git
git checkout ROS2_field_description
cd your_folder/ros2_ws
export GZ_SIM_RESOURCE_PATH="your_folder/ros2_ws/src/leonardo_field_description/models"
colcon build
. install/setup.bash
ros2 launch leonardo_field_description launch_leonardo_race_field.py
```
# Note
Execute the command:
```sh
export GZ_SIM_RESOURCE_PATH="your_folder/ros2_ws/src/leonardo_field_description/models"
```
every time the system is rebooted or if the environment variable is changed for other purposes.
