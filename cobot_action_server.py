import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_interfaces.action import SetAngle

# for mycobot,mecharm
from pymycobot.mycobot import MyCobot

# Set-up Cobot Phase -----
mycobot = MyCobot("/dev/ttyAMA0", 115200)

# -----

class SetAngleActionServer(Node):

    def __init__(self):
        super().__init__('set_angle_action_server')
        self._action_server = ActionServer(
            self,
            SetAngle,
            'set_angle',
            self.execute_callback)
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        mycobot.SetAngle(goal_handle.request.angles, 80)

        goal_handle.succeed()

        result = SetAngle.Result()
        result.result = True
        return result
    
def main(args=None):

    rclpy.init(args=args)

    set_angle_action_server = SetAngleActionServer()

    rclpy.spin(set_angle_action_server)

if __name__ == '__main__':
    main()