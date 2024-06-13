import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('imu_publisher'), 'config')
    ekf_config = LaunchConfiguration('ekf_config', default=os.path.join(config_dir, 'ekf_config.yaml'))

    return LaunchDescription([
        DeclareLaunchArgument(
            'ekf_config',
            default_value=ekf_config,
            description='Path to the EKF configuration file.'
        ),

        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config]
        )
    ])
