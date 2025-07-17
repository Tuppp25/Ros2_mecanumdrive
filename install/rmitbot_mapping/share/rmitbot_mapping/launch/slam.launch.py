import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription

# ros2 launch rmitbot_mapping slam.launch.py use_sim_time:=true
# ros2 launch rmitbot_mapping slam.launch.py use_sim_time:=false

def generate_launch_description():
    use_sim_arg = DeclareLaunchArgument(
        'use_sim',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )
    
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen', 
        parameters=[
            os.path.join(get_package_share_directory("rmitbot_mapping"), "config", "slam.yaml"), 
            {'use_sim_time': LaunchConfiguration('use_sim_time')}
        ],
    )
    yaml_path = os.path.join(get_package_share_directory("rmitbot_mapping"), "config", "slam.yaml")
    print("YAML Path:", yaml_path) 
    
    slam_launch = IncludeLaunchDescription(
        os.path.join(get_package_share_directory("slam_toolbox"),"launch","online_async_launch.py"),
        launch_arguments={
            'params_file': os.path.join(get_package_share_directory("rmitbot_mapping"), "config", "slam.yaml"), 
            'use_sim_time': LaunchConfiguration('use_sim'), 
            }.items()
    )
    
    rplidar_node = Node(
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
    
    
    return LaunchDescription([
        use_sim_arg, 
        slam_launch,
    ])
    # Command line
    # ros2 launch slam_toolbox online_async_launch.py params_file:=./scr/rmitbot_mapping/config/slam.yaml use_sim_time:=true