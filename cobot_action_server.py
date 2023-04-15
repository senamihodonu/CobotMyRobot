#!/bin/python3

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_interfaces.action import SetAngle, PickUP

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

        ####
        mycobot.set_gripper_state(0, 50)
        mycobot.wait(3)
        mycobot.send_angles(goal_handle.request.angles, goal_handle.request.speed)
        mycobot.wait(1)
        mycobot.send_coords([288.9,-87.5,190.9,167.43,0.6,-90.22], 50, 0)
        mycobot.wait(2)
        mycobot.send_coords([288.9,-87.5,190.9,150.07,0.6,-90.22], 50, 0)
        mycobot.wait(5)
        mycobot.set_gripper_state(1, 50)
        ####
        while(mycobot.is_moving()):
            print("Cobot in motion")
            mycobot.wait(1)

        goal_handle.succeed()

        result = SetAngle.Result()
        # result.end_angles = mycobot.get_angles()
        return result
    
class PickUPActionServer(Node):

    def __init__(self):
        super().__init__('pick_up_action_server')
        self._action_server = ActionServer(
            self,
            PickUP,
            'pickup',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        grip = 0 if goal_handle.request.open else 1
        goalComplete = True
        try:
            mycobot.set_gripper_state(grip, 50)
            mycobot.wait(2)
        except Exception as e:
            print(f'{e}')
            goalComplete = False

        goal_handle.succeed()

        result = PickUP.Result()
        result.status = goalComplete
        return result

def main(args=None):

    rclpy.init(args=args)

    actionQueue = []
    actionQueue.append(SetAngleActionServer())
    actionQueue.append(PickUPActionServer())

    while rclpy.ok():
        try:
            for node in actionQueue:
                rclpy.spin_once(node, timeout_sec=(0.01 / len(actionQueue)))
        except:
            print("An action queue error has occured")
            rclpy.shutdown()


if __name__ == '__main__':
    main()