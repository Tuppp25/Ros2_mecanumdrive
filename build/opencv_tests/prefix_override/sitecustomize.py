import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ngan/Documents/test_github/lesson6_ws/install/opencv_tests'
