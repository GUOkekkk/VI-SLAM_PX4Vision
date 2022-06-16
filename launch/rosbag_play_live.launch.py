import launch


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'play','/home/nfrancinelli/rosbag/rosbag_hand/rosbag2_2022_06_02-10_07_12_0.db3', '--clock'],
            output='screen'
        )
    ])
