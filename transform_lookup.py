#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener, Buffer
import geometry_msgs.msg

class TransformLookup(Node):

    def __init__(self):
        super().__init__('transform_lookup')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Create a timer to periodically check for the transform
        self.timer = self.create_timer(1.0, self.lookup_transform)

    def lookup_transform(self):
        try:
            now = rclpy.time.Time()
            # Specify the target and source frames
            transform = self.tf_buffer.lookup_transform('arm_camera_color_frame', 'lidar_link', now)
            self.get_logger().info('Transform from lidar to camera: %s' % transform)
        except Exception as e:
            self.get_logger().warn('Could not transform lidar to camera: %s' % str(e))

def main(args=None):
    rclpy.init(args=args)
    node = TransformLookup()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()