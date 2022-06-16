from simple_launch import SimpleLauncher

def generate_launch_description():
    '''
    Launch description for project defense presentation
    '''
    sl = SimpleLauncher(use_sim_time = True)
    
    # conditional args
    sl.declare_arg('offline_mapping', default_value = True, description='Replay previous SLAM')
    sl.declare_arg('rviz', default_value=True, description='Bringup RViz2')

    with sl.group(if_arg='offline_mapping'):
        sl.include('tf2_broadcaster', 'rosbag_play.launch.py')
    with sl.group(unless_arg='offline_mapping'):
        sl.include('tf2_broadcaster','rosbag_play_live.launch.py')
        sl.include('tf2_broadcaster','cartographer.launch.py')
    
    sl.include('tf2_broadcaster', 'rosbag_test_launch.py') 
    
    with sl.group(if_arg='rviz'):
        sl.include('structure_core_ros2_driver','rviz_launch.py')        
        
    return sl.launch_description()
