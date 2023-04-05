import rclply
from rclpy.action import ActionServer
from rclpy.node import Node

from cobot_action_interface import SetAngle

class SetAngleActionServer(Node):

    def __init__(self):
        super.__init__('set_angle_action_server')
        self._action_server = ActionServer(
            self,
            SetAngle,
            'set_angle',
            self.execute_callback)
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        result = SetAngle.Result()
        return result
    
def main(args=None):
    rclply.init(args=args)

    set_angle_action_server = SetAngleActionServer()

    rclpy.spin(set_angle_action_server)

if __name__ == '__main__':
    main()