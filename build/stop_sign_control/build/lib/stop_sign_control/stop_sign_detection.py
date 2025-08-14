# ROS2 module imports
import rclpy # ROS2 client library (rcl) for Python (built on rcl C API)
from rclpy.node import Node # Node class for Python nodes
from geometry_msgs.msg import Twist # Twist (linear and angular velocities) message class
from darknet_ros_msgs.msg import BoundingBoxes # BoundingBoxes (Tiny-YOLO object detections) message class
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy # Ouality of Service (tune communication between nodes)
from rclpy.duration import Duration # Time duration class

# Python mudule imports
from math import inf # Common mathematical constant

# Node class
class RobotController(Node):

    #######################
    '''Class constructor'''
    #######################

    def __init__(self):
        # Information and debugging
        info = '\nMake the robot stop if a stop sign is detected within a threshold distance.\n'
        print(info)
        # ROS2 infrastructure
        super().__init__('robot_controller') # Create a node with name 'robot_controller'
        qos_profile = QoSProfile( # Ouality of Service profile
        reliability=QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE, # Reliable (not best effort) communication
        history=QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST, # Keep/store only up to last N samples
        depth=10 # Queue size/depth of 10 (only honored if the “history” policy was set to “keep last”)
        )
        self.robot_yolo_sub = self.create_subscription(BoundingBoxes, '/darknet_ros/bounding_boxes', self.robot_yolo_callback, qos_profile) # Subscriber which will subscribe to BoundingBoxes message on the topic '/darknet_ros/bounding_boxes' adhering to 'qos_profile' QoS profile
        self.robot_yolo_sub # Prevent unused variable warning
        self.robot_ctrl_pub = self.create_publisher(Twist, '/cmd_vel', qos_profile) # Publisher which will publish Twist message to the topic '/cmd_vel' adhering to 'qos_profile' QoS profile
        timer_period = 0.001 # Node execution time period (seconds)
        self.timer = self.create_timer(timer_period, self.robot_controller_callback) # Define timer to execute 'robot_controller_callback()' every 'timer_period' seconds
        self.detection = None # Initialize variable to capture the YOLO detection
        self.detection_available = False # Initialize variable to capture availability of YOLO detection
        self.detected_stop_sign = False # Flag to indicate detection of stop sign
        self.obeyed_stop_sign = False # Flag to indicate obedience of stop sign
        self.ctrl_msg = Twist() # Robot control commands (twist)
        self.start_time = self.get_clock().now() # Record current time in seconds
        self.stop_time = inf # Time elapsed since complete stop

    ########################
    '''Callback functions'''
    ########################

    def robot_yolo_callback(self, msg):
        # Ensure there is at least one bounding box detected before trying to access it
        if msg.bounding_boxes:
            self.detection = msg.bounding_boxes[0] # Capture most recent YOLO detection
            self.detection_available = True # Set YOLO detection flag to available
        else:
            self.detection = None
            self.detection_available = False


    def robot_controller_callback(self):
        THRESH = 750 # Stop sign threshold area to come to a complete stop (px squared)
        LIN_VEL_X = 0.1 # Linear velocity (m/s) forward/backward
        LIN_VEL_Y = 0.1 # Linear velocity (m/s) for strafing left/right
        ANG_VEL_Z = 0.0 # Angular velocity (rad/s) for turning
        DELAY = 4.0 # Time delay (s)
        
        # Check if we have received a detection and enough time has passed
        if self.get_clock().now() - self.start_time > Duration(seconds=DELAY) and self.detection_available:
            
            # Use a temporary variable for the bounding box to avoid potential errors
            # if the detection is updated mid-function.
            current_detection = self.detection

            # Make sure we have a valid detection before proceeding
            if current_detection is not None:
                detection = current_detection.class_id # Class ID (label) of YOLO object detection
                probability = current_detection.probability # Probability (confidence) of prediction
                box_length = current_detection.xmax - current_detection.xmin # Length of bounding box
                box_height = current_detection.ymax - current_detection.ymin # Height of bounding box
                box_area = box_length * box_height # Area of bounding box

                # Stop for some time if stop sign detected within thresholded distance
                if self.obeyed_stop_sign==False and detection=='stop sign' and probability>0.6 and box_area>THRESH:
                    self.ctrl_msg.linear.x = 0.0 # Set linear velocity to stop
                    self.ctrl_msg.linear.y = 0.0 # <--- IMPORTANT: Also set strafing velocity to stop
                    self.ctrl_msg.angular.z = 0.0 # Set angular velocity to stop
                    self.robot_ctrl_pub.publish(self.ctrl_msg) # Publish robot controls message
                    
                    # Start timer
                    if self.detected_stop_sign==False:
                        self.stop_time = self.get_clock().now() # Record current time in seconds
                        self.detected_stop_sign = True
                    
                    # Stop at stop sign for `DELAY` amount of seconds
                    if self.get_clock().now() - self.stop_time > Duration(seconds=DELAY):
                        self.obeyed_stop_sign = True
                    
                    print('Obeying the detected stop sign!')
                
                # Continue with motion
                else:
                    # Example of how to use linear.y for a Mecanum robot
                    # This logic is just for demonstration. You would replace this with
                    # your own control logic based on object location, etc.
                    # For example, if the stop sign is to the right, you could strafe left to avoid it.
                    # Here we simply set a forward motion and a small strafe to the left.
                    self.ctrl_msg.linear.x = min(0.22, LIN_VEL_X) # Set forward linear velocity
                    self.ctrl_msg.linear.y = min(0.1, -LIN_VEL_Y) # <--- IMPORTANT: Set strafing velocity (negative is left)
                    self.ctrl_msg.angular.z = min(2.84, ANG_VEL_Z) # Set angular velocity
                    self.robot_ctrl_pub.publish(self.ctrl_msg) # Publish robot controls message
                    # print('Continuing with motion...')
            else:
                # If no detection is available, just move forward
                self.ctrl_msg.linear.x = min(0.22, LIN_VEL_X)
                self.ctrl_msg.linear.y = 0.0 # Stop strafing if no object is detected
                self.ctrl_msg.angular.z = 0.0
                self.robot_ctrl_pub.publish(self.ctrl_msg)
                print('No detection available, moving forward.')

        else:
            print('Initializing or waiting for first detection...')

def main(args=None):
    rclpy.init(args=args) # Start ROS2 communications
    node = RobotController() # Create node
    rclpy.spin(node) # Execute node
    node.destroy_node() # Destroy node explicitly (optional - otherwise it will be done automatically when garbage collector destroys the node object)
    rclpy.shutdown() # Shutdown ROS2 communications

if __name__ == "__main__":
    main()
