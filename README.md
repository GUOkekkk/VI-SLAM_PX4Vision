# Abstract
The aim of this project is to perform visual simultaneous localization and
mapping with an UAV (Unmanned Aerial Vehicle). The drone used for this
project is a PX4 Vision equipped with a Structure Core sensor. ROS2 is used,
along several packages available: (1) the Cartographer package for mapping
and localisation, (2) the ls2n_drone_ros2 packages to control drone motions.
The first step of the project was to get an understanding of the packages.
Then, to use the sensor SDK combined with Cartographer to perform SLAM.
And, finally, using the obtained 3D map to track some trajectories with the
UAV. The experiments were performed in the LS2N drone arena. The project report and result video could be found in this repository.

The result is shown as below:
![result](https://github.com/GUOkekkk/VSLAM_PX4Vision/blob/main/Result.png)

# Package installation

Compile in a ROS2 Workspace.

# Package use

Launch the tf2 nodes using the launch file:

~~~
ros2 launch tf2_broadcaster rosbag_test_launch.py
~~~

After, launch the cartographer node:

~~~
ros2 launch tf2_broadcaster cartographer.launch.py 
~~~

Use 'use_sim_time:=True' if working with a rosbag.

Finally we put all code in one launch file,so just run
~~~
ros2 launch tf2_broadcaster presentation.launch.py
~~~
By the way the condition to run the above code it that the [simple launch](https://github.com/oKermorgant/simple_launch) moudle is already installed in the computer.
