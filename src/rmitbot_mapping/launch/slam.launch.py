import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'frame_id': 'laser_link',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])
    # Command line
    # ros2 launch slam_toolbox online_async_launch.py params_file:=./scr/rmitbot_mapping/config/mapper_params_online_async.yaml use_sim_time:=true
