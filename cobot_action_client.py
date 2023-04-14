import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_interfaces.action import SetAngle

from pymycobot.mycobot import MyCobot

# mycobot = MyCobot("/dev/ttyAMA0", 115200)

class SetAngleActionClient(Node):

    def __init__(self):
        super().__init__('set_angle_action_server')
        self._action_client = ActionClient(self, SetAngle, 'set_angle')

    def send_goal(self, angles, speed):
        goal_msg = SetAngle.Goal()
        goal_msg.angles = angles
        goal_msg.speed = speed

        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client =  SetAngleActionClient()
    angles = [0.0,0.0,0.0,0.0,0.0,0.0]
    speed = 50

    future = action_client.send_goal(angles, speed)

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()