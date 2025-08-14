from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Use the correct package name for darknet
    pkg_darknet_ros = get_package_share_directory('darknet_ros')

    # Path to the darknet-ros launch file
    darknet_ros_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([pkg_darknet_ros, '/launch/darknet_ros.launch.py'])
    )


    return LaunchDescription([
        # Launch darknet-ros
        darknet_ros_launch,

        # Launch the custom stop sign detection script
        Node(
            package='stop_sign_control',
            executable='stop_sign_detection',  # must match setup.py entry point
            name='stop_sign_detection',
            output='screen',
        ),

    ])