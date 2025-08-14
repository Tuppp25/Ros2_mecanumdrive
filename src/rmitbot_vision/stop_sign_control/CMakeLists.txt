cmake_minimum_required(VERSION 3.5)
project(stop_sign_detection)

# find ament_cmake and ament_cmake_python
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

# This is the core command for a Python package.
# It installs everything from the python_pkg directory into your install space.
ament_python_install_package(${PROJECT_NAME})

ament_package()