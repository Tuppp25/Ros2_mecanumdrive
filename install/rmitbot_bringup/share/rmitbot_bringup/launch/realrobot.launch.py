import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, RegisterEventHandler, ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    hardware_interface = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_firmware"),
            "launch",
            "hardware_interface.launch.py"
        ),
    )
    
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_controller"),
            "launch",
            "controller.launch.py"
        ),
    )
    
    teleopkeyboard = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_controller"),
            "launch",
            "teleopkeyboard.launch.py"
        ),
        launch_arguments={
            "use_sim_time": "False"
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
        launch_arguments={"use_sim": "false"}.items()
        # launch_arguments={"use_sim": LaunchConfiguration('use_sim')}.items()
    )

    rviz = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_description"),
            "launch",
            "display.launch.py"
        ),
    )
    twistmux = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_mapping"),
            "launch",
            "twistmux.launch.py"
        ),
    )

    navigation = IncludeLaunchDescription(
        os.path.join(get_package_share_directory("rmitbot_mapping"),"launch","nav2_slam.launch.py"),
        launch_arguments={"use_sim": "false"}.items()
        # launch_arguments={"use_sim": LaunchConfiguration('use_sim')}.items()
    )
        # === Bridge node to convert /cmd_vel (Twist) → /rmitbot_controller/reference (TwistStamped) ===


    # imu_driver_node = Node(
    #     package="bumperbot_firmware",
    #     executable="mpu6050_driver.py"
    # )
    navigation_delayed = TimerAction(
        period = 10., 
        actions=[navigation]
    )
    
    return LaunchDescription([
        # hardware_interface,
        # controller,
        # teleopkeyboard,
        # imu_driver_node,
        localization,
        mapping_launch,
        navigation_delayed,
        rviz,
        twistmux,

    ])