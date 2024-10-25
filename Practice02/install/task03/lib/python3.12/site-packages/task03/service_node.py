import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ServiceNode(Node):
    def __init__(self):
        super().__init__('service_node')

        self.declare_parameter('service_name', '/trigger_service')
        self.declare_parameter('default_string', 'No service available')

        self.service_name = self.get_parameter('service_name').get_parameter_value().string_value
        self.default_string = self.get_parameter('default_string').get_parameter_value().string_value
        self.stored_string = self.default_string

        self.client = self.create_client(Trigger, '/spgc/trigger')
        self.call_service()

        self.service = self.create_service(
            Trigger,
            self.service_name,
            self.handle_service_request
        )
        self.get_logger().info(f'Service node ready, providing service: {self.service_name}')

    def call_service(self):
        if not self.client.wait_for_service(timeout_sec=5.0):
            self.get_logger().warn('Service /spgc/trigger not available. Using default string.')
            self.stored_string = self.default_string
            return

        request = Trigger.Request()
        future = self.client.call_async(request)
        future.add_done_callback(self.service_callback)

    def service_callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.stored_string = response.message
                self.get_logger().info(f'Received from /spgc/trigger: "{self.stored_string}"')
            else:
                self.stored_string = self.default_string
                self.get_logger().warn(f'Service call failed, using default string: "{self.default_string}"')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')
            self.stored_string = self.default_string

    def handle_service_request(self, request, response):
        response.success = True
        response.message = self.stored_string
        self.get_logger().info(f'Responding with: "{self.stored_string}"')
        return response

def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()
    try:
        rclpy.spin(service_node)
    except KeyboardInterrupt:
        pass
    finally:
        service_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
