#!/bin/python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from rclpy.qos import qos_profile_sensor_data
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from geometry_msgs.msg import PoseStamped
from action_msgs.msg._goal_status import GoalStatus

import irobot_create_msgs
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle,NavigateToPosition, Dock
from irobot_create_msgs.srv._reset_pose import ResetPose
from irobot_create_msgs.msg import HazardDetectionVector

from pynput.keyboard import KeyCode
from key_commander import KeyCommander
from threading import Lock, RLock
from rclpy.executors import MultiThreadedExecutor
from random import uniform, choices

from action_interfaces.action import SetAngle, PickUP

from pymycobot.mycobot import MyCobot

import time

import Create3

# mycobot = MyCobot("/dev/ttyAMA0", 115200)

speed = 50
sleep_time = 1

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
    

class PickUpActionClient(Node):

    def __init__(self):
        super().__init__('pick_up_action_server')
        self._action_client = ActionClient(self, PickUP, 'pickup')

    def send_goal(self, open):
        goal_msg = PickUP.Goal()
        goal_msg.open = open

        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)
    

def PickUpCube():
    action_client =  SetAngleActionClient()
    angles = [0.0,0.0,0.0,0.0,0.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    ## Approach
    action_client =  PickUpActionClient()
    open = True
    future = action_client.send_goal(open)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [0.0,0.0,-85.0,20.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [0.0,-20.0,-85.0,20.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    time.sleep(2)

    action_client =  PickUpActionClient()
    open = False
    future = action_client.send_goal(open)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [0.0,0.0,-81.5,20.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [60.0,0.0,-81.5,20.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

def HoldCube():
    print('new program')
    

def DropOffCube():
    time.sleep(2)

    action_client =  PickUpActionClient()
    open = True
    future = action_client.send_goal(open)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [60.0,0.0,-81.5,40.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    time.sleep(2)
    action_client =  SetAngleActionClient()
    angles = [60.0,-5.0,-81.5,25.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  PickUpActionClient()
    open = False
    future = action_client.send_goal(open)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [0.0,0.0,-67.0,20.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)


    action_client =  SetAngleActionClient()
    angles = [0.0,-20.0,-85.0,20.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    time.sleep(2)

    action_client =  PickUpActionClient()
    open = True
    future = action_client.send_goal(open)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [0.0,-20.0,-85.0,40.0,90.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)

    action_client =  SetAngleActionClient()
    angles = [0.0,0.0,0.0,0.0,0.0,0.0]
    future = action_client.send_goal(angles, speed)
    rclpy.spin_until_future_complete(action_client, future)
    

def main(args=None):
    rclpy.init(args=args)
    PickUpCube()
    Create3.create()
    DropOffCube()


if __name__ == '__main__':
    main()