import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('nav2_bringup'),
                'launch',
                'navigation_launch.py'
            ])
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'params_file': os.path.join(get_package_share_directory('rmitbot_mapping'),
                                        'config', 'nav2_params.yaml'),
            # 'cmd_vel': '/nav2/cmd_vel',
            # 'ros_arguments': '--ros-args -r /cmd_vel:=/nav2/cmd_vel', 
        }.items(), 

    )

    return LaunchDescription([nav2_launch])