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
