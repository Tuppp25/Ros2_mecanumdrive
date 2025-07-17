import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    rviz = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_description"),
            "launch",
            "display.launch.py"
        ),
    )
    # Launch Gazebo with the robot model
    gazebo = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_description"),
            "launch",
            "gazebo.launch.py"
        ),
    )
    
    # Launch the controller manager
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_controller"),
            "launch",
            "controller.launch.py"
        ),
    )
    
    # Launch the teleop keyboard node
    teleopkeyboard = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_controller"),
            "launch",
            "teleopkeyboard.launch.py"
        ),
        launch_arguments={
            "use_sim_time": "True"
        }.items()
    )
    
    localization = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_localization"),
            "launch",
            "local_localization.launch.py"
        ),
    )
    
    mapping_launch = IncludeLaunchDescription(
        os.path.join(get_package_share_directory("rmitbot_mapping"),"launch","slam.launch.py"),
        launch_arguments={"use_sim": "true"}.items()
        # launch_arguments={"use_sim": LaunchConfiguration('use_sim')}.items()
    )
    
    
    return LaunchDescription([
        rviz,
        gazebo,
        controller,
        teleopkeyboard,
        localization,
        mapping_launch, 
    ])