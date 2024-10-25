import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.declare_parameter('text', 'Hello, ROS2!')
        self.declare_parameter('topic_name', '/spgc/receiver')

        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        self.publisher_ = self.create_publisher(String, topic_name, 10)
        self.timer = self.create_timer(1.0, self.publish_message)

        self.get_logger().info(f'Publishing to topic: {topic_name}')

    def publish_message(self):
        message = String()
        message.data = self.get_parameter('text').get_parameter_value().string_value
        self.publisher_.publish(message)
        self.get_logger().info(f'Published message: "{message.data}"')

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    try:
        rclpy.spin(publisher_node)
    except KeyboardInterrupt:
        pass
    finally:
        publisher_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
