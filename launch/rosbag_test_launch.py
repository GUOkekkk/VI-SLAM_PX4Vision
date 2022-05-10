import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration,TextSubstitution

def generate_launch_description():
    
    ns = LaunchConfiguration('ns')
    config = LaunchConfiguration('config')

    sc_config_path = os.path.join(get_package_share_directory( 'tf2_broadcaster' ), 'cfg')
    
    sc_config_file = [TextSubstitution(text=sc_config_path+'/'),
                 config, TextSubstitution(text='_config.yaml')]

    os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '{time}: [{name}] [{severity}] - {message}'
    
    imu_frame = [ns, TextSubstitution(text='_imu')]
    rgb_frame = [ns, TextSubstitution(text='_rgb')]
    depth_frame = [ns, TextSubstitution(text='_depth')]
    odom_frame = 'odom'

    return LaunchDescription( [
        DeclareLaunchArgument('ns', default_value='sc'),
        DeclareLaunchArgument('config', default_value='sc'),
        
        #Publish map -> drone transform
        Node(package='tf2_broadcaster',
             executable='tf2_broadcaster',
             name='tf2_broadcaster_node',
             output='screen',
             parameters=[
             	{'topic_name_': '/Drone9/EKF/odom'}
             ]      
        ),
        Node(package='tf2_ros',
             executable='static_transform_publisher',
             name='sc_cam_tf',
             arguments=['0', '0', '0',  '0', '0', '0', depth_frame, rgb_frame]),
             
        Node(package='tf2_ros',
             executable='static_transform_publisher',
             name='sc_imu_tf',             
             arguments=['0', '0', '0',  '0', '0', '0', depth_frame, imu_frame]),
                # xyz roll pitch yaw
        Node(package='tf2_ros',
     	     executable='static_transform_publisher',
     	     name='sc_drone_cam_tf',
     	     arguments=['0', '0', '0',  '0', '0', '0', odom_frame, depth_frame])
                
        #TODO GET REAL PARAMS ROBOT_FRAME -> CAMERA_FRAME TF
        #TODO MODIFY CAMERA -> IMU TF
                
])
