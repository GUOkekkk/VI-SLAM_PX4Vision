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
    drone_frame = 'base_link'

    return LaunchDescription( [
        DeclareLaunchArgument('ns', default_value='sc'),
        DeclareLaunchArgument('config', default_value='sc'),
        
        #Publish map -> drone transform
        Node(package='tf2_broadcaster',
             executable='tf2_broadcaster',
             name='tf2_broadcaster_node',
             output='screen',
             parameters=[
             	{'topic_name_': '/Drone9/EKF/odom'},
             	{'use_sim_time': True}
             ]      
        ),
        Node(package='tf2_ros',
             executable='static_transform_publisher',
             name='sc_cam_tf',
             arguments=['0', '0', '0',  '0', '0', '0', depth_frame, rgb_frame],
             parameters=[{'use_sim_time': True}]
        ),
             
        Node(package='tf2_ros',
             executable='static_transform_publisher',
             name='sc_imu_tf',             
             arguments=['0', '0', '0',  '-1.57', '0', '1.57', depth_frame, imu_frame],
             parameters=[{'use_sim_time': True}]
            ),

                # xyz yaw pitch roll
        Node(package='tf2_ros',
     	     executable='static_transform_publisher',
     	     name='sc_drone_cam_tf',
     	     arguments=['0', '0', '0',  '0', '0', '-1.57', drone_frame, depth_frame],
	     parameters=[{'use_sim_time': True}]
     	     ),
     	 
     	#KEEP THIS ONLY FOR WORKING WITH OLD BAGFILES
     	Node(package='tf2_ros',
     	     executable='static_transform_publisher',
     	     name='sc_depth_tf',
     	     arguments=['0', '0', '0',  '0', '0', '0', depth_frame, 'sc_depth_frame'],
             parameters=[{'use_sim_time': True}]
     	     
     	     )
     	   
     	#Node(package='tf2_broadcaster',
     	#     executable='republisher',
     	#     name='republisher_odom_node',
     	#     output='screen',
     	#     parameters=[
        #     	{'topic_name_': '/Drone9/EKF/odom'}
        #     ]
        #) 
        
        #TODO TRANSLATIONS OF STATIC TRANSFORMS BASE_LINK -> CAMERA
                
])
