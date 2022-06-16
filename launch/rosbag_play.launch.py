import launch


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'play','/home/nfrancinelli/rosbag/live_mapping/live_mapping_0.db3', '--clock'],
            output='screen'
        )
    ])
