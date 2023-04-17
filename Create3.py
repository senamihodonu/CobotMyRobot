import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
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

from time import sleep

# To help with Multithreading
lock = RLock()
# Number of random walk
rand_walks = 5
# rand walk angle limit
max_angle = 4.70
namespace = 'create3_05AE'
# namespace = 'create3_05AE'

class Slash(Node):
    """
    Class to coordinate actions and subscriptions
    """

    def __init__(self, namespace):
        super().__init__('slasher')

        # 2 Seperate Callback Groups for handling the bumper Subscription and Action Clients
        cb_Subscripion = MutuallyExclusiveCallbackGroup()
        #cb_Action = cb_Subscripion
        cb_Action =MutuallyExclusiveCallbackGroup()
        cb_srv = MutuallyExclusiveCallbackGroup()

        # Subscription to Hazards, the callback function attached only looks for bumper hits
        self.subscription = self.create_subscription(
            HazardDetectionVector, f'/{namespace}/hazard_detection', self.listener_callback, qos_profile_sensor_data,callback_group=cb_Subscripion)

        # Action clients for movements
        self._undock_ac = ActionClient(self, Undock, f'/{namespace}/undock',callback_group=cb_Action)
        self._dock_ac = ActionClient(self, Dock, f'/{namespace}/dock',callback_group=cb_Action)
        self._drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance',callback_group=cb_Action)
        self._rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle', callback_group=cb_Action)
        self._nav_ac = ActionClient(self, NavigateToPosition, f'/{namespace}/navigate_to_position', callback_group=cb_Action)
        
        self.reset = self.create_client(ResetPose, f'/{namespace}/reset_pose', callback_group=cb_srv)
        self.req = ResetPose.Request()

        # Variables
        self._goal_uuid = None



    def listener_callback(self, msg):
        '''
        This function is called every time self.subscription gets a message
        from the Robot. Here it parses the message from the Robot and if its
        a 'bump' message, cancel the current action. 

        For this to work, make sure you have:
        ros__parameters:
            reflexes_enabled: false
        in your Application Configuration Parameters File!!!
        '''

        # If it wasn't doing anything, there's nothing to cancel
        if self._goal_uuid is None:
            return

        # msg.detections is an array of HazardDetection from HazardDetectionVectors.
        # Other types can be gotten from HazardDetection.msg
        for detection in msg.detections:
            if detection.type == 1:   #If it is a bump
                self.get_logger().warning('HAZARD DETECTED')
                with lock: # Make this the only thing happening
                    self.get_logger().warning('CANCELING GOAL')           
                    self._goal_uuid.cancel_goal_async()
                    # Loop until the goal status returns canceled
                    while self._goal_uuid.status is not GoalStatus.STATUS_CANCELED:
                        pass    
                    print('Goal canceled.')
                    backup_goal = DriveDistance.Goal()
                    backup_goal.distance = -0.1
                    self.sendDriveGoal(backup_goal)

                    rotate_goal = RotateAngle.Goal()
                    numbers_list = [-3.142,3.142]
                    rotate_goal.angle = choices(numbers_list)
                    print(rotate_goal.angle)
                    self.sendRotateGoal(rotate_goal)

                    drive_goal = DriveDistance.Goal()
                    drive_goal.distance = 0.5
                    self.sendDriveGoal(drive_goal)

#--------------------Async send goal calls-----------------------------
    def sendDriveGoal(self,goal):
        """
        Sends a drive goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            self.get_logger().warning('WAITING FOR Drive SERVER')
            self._drive_ac.wait_for_server()
            self.get_logger().warning('SERVER AVAILABLE')

            self.get_logger().warning('Sending Drive goal')
            drive_handle = self._drive_ac.send_goal_async(goal)
            self.get_logger().warning('Waiting for Future')
            while not drive_handle.done():
                pass # Wait for Action Server to accept goal
            self.get_logger().warning('Retrieving Future')
            # Hold ID in case we need to cancel it
            self._goal_uuid = drive_handle.result() 

        self.get_logger().warning('Waiting for unknown')
        while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
            pass # Wait until a Status has been assigned
        
        self.get_logger().warning('Waiting for cancel/Success')
        # After getting goalID, Loop while the goal is currently running
        while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
            if self._goal_uuid.status is GoalStatus.STATUS_CANCELED:
                break # If the goal was canceled, stop looping otherwise loop till finished
            pass

        self.get_logger().warning('Waiting to reset goal ID')
        with lock:
            # Reset the goal ID, nothing should be running
            self._goal_uuid = None 

    def sendRotateGoal(self,goal):
        """
        Sends a Rotate goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            self.get_logger().warning('WAITING FOR Rotate SERVER')
            self._rotate_ac.wait_for_server()
            self.get_logger().warning('SERVER AVAILABLE')

            self.get_logger().warning('Sending rotate goal')
            drive_handle = self._rotate_ac.send_goal_async(goal)
            self.get_logger().warning('Waiting for Future')
            while not drive_handle.done():
                pass # Wait for Action Server to accept goal
            self.get_logger().warning('Retrieving Future')
            # Hold ID in case we need to cancel it
            self._goal_uuid = drive_handle.result() 

        self.get_logger().warning('Waiting for unknown')
        while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
            pass # Wait until a Status has been assigned
        
        self.get_logger().warning('Waiting for cancel/Success')
        # After getting goalID, Loop while the goal is currently running
        while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
            if self._goal_uuid.status is GoalStatus.STATUS_CANCELED:
                break # If the goal was canceled, stop looping otherwise loop till finished
            pass
        
        self.get_logger().warning('Waiting to reset goal ID')
        with lock:
            # Reset the goal ID, nothing should be running
            self._goal_uuid = None 

    def sendNavGoal(self,goal):
        """
        Sends a Rotate goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            self.get_logger().warning('WAITING FOR NAV SERVER')
            self._nav_ac.wait_for_server()
            self.get_logger().warning('SERVER AVAILABLE')

            self.get_logger().warning('Sending NAV goal')
            drive_handle = self._nav_ac.send_goal_async(goal)
            self.get_logger().warning('Waiting for Future')
            while not drive_handle.done():
                pass # Wait for Action Server to accept goal
            self.get_logger().warning('Retrieving Future')
            # Hold ID in case we need to cancel it
            self._goal_uuid = drive_handle.result() 

        self.get_logger().warning('Waiting for unknown')
        while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
            print("navigating")
            # pass # Wait until a Status has been assigned
        
        self.get_logger().warning('Waiting for cancel/Success')
        # After getting goalID, Loop while the goal is currently running
        while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
            if self._goal_uuid.status is GoalStatus.STATUS_CANCELED:
                break # If the goal was canceled, stop looping otherwise loop till finished
            pass
        
        self.get_logger().warning('Waiting to reset goal ID')
        with lock:
            # Reset the goal ID, nothing should be running
            self._goal_uuid = None 

    def sendDocGoal(self,goal):
        """
        Sends a Rotate goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            self.get_logger().warning('WAITING FOR NAV SERVER')
            self._dock_ac.wait_for_server()
            self.get_logger().warning('SERVER AVAILABLE')

            self.get_logger().warning('Sending NAV goal')
            drive_handle = self._dock_ac.send_goal_async(goal)
            self.get_logger().warning('Waiting for Future')
            while not drive_handle.done():
                pass # Wait for Action Server to accept goal
            self.get_logger().warning('Retrieving Future')
            # Hold ID in case we need to cancel it
            self._goal_uuid = drive_handle.result() 

        self.get_logger().warning('Waiting for unknown')
        while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
            pass # Wait until a Status has been assigned
        
        self.get_logger().warning('Waiting for cancel/Success')
        # After getting goalID, Loop while the goal is currently running
        while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
            if self._goal_uuid.status is GoalStatus.STATUS_CANCELED:
                break # If the goal was canceled, stop looping otherwise loop till finished
            pass
        
        self.get_logger().warning('Waiting to reset goal ID')
        with lock:
            # Reset the goal ID, nothing should be running
            self._goal_uuid = None 
#----------------------------------------------------------------------

    def WalkOfShame(self):
        self.get_logger().warning('Walk of shame')
        for i in range(0,rand_walks):
            self.get_logger().warning('Loop: ' + str(i))

            rotate_goal = RotateAngle.Goal()
                
            rotate_goal.angle = uniform(-max_angle, max_angle)

            self.get_logger().warning('----------------------------------')
            self.get_logger().warning('Rotating ' + str(rotate_goal.angle))
            self.get_logger().warning('----------------------------------')
            self.sendRotateGoal(rotate_goal)
            self.get_logger().warning('DONE Rotating')

            self.get_logger().warning('Driving')
            drive_goal = DriveDistance.Goal()
            drive_goal.distance = 0.75

            self.sendDriveGoal(drive_goal)
            self.get_logger().warning('DONE Driving')

    
    def navigate(self):
        """
        Undocks robot and drives out a meter asynchronously
        """
        # Freshly started, undock
        self.get_logger().warning('WAITING FOR SERVER')
    # wait until the robot server is found and ready to receive a new goal
        self._undock_ac.wait_for_server()
        self.get_logger().warning('SERVER AVAILABLE')
        self.get_logger().warning('UNDOCKING')

    # create new Undock goal object to send to server
        undock_goal = Undock.Goal()
        self._undock_ac.send_goal(undock_goal)
        self.get_logger().warning('UNDOCKED')

    # create goal object and drive 0.5m to return postion
        drive_goal1 = DriveDistance.Goal()
        drive_goal1.distance = 1.75
    # send goal to async function
        self.get_logger().warning('Driving ' + str(drive_goal1.distance) + ' meters to return position')
        self.sendDriveGoal(drive_goal1)
        self.get_logger().warning('Done Driving')

    # create goal object to rotate 180
        rotate_goal = RotateAngle.Goal()
        rotate_goal.angle = 3.142
    # send goal to async function
        self.sendRotateGoal(rotate_goal)
        self.get_logger().warning('DONE Rotating')

    # # reset odometer
    #     self.get_logger().warning('RESETTING POSE')
    #     self.reset.call(self.req)
    # #capture return position
    #     self.get_logger().warning('ACQUIRING POSE')
    #     self.pose = PoseStamped() 

    # # create goal object and specify distance to drive
    #     drive_goal = DriveDistance.Goal()
    #     drive_goal.distance = 0.6
    # # send goal to async function
    #     self.get_logger().warning('Driving ' + str(drive_goal.distance))
    #     self.sendDriveGoal(drive_goal)
    #     self.get_logger().warning('Done Driving')

    #     self.WalkOfShame()

    #  # navigate to return position       
    #     nav_pos = NavigateToPosition.Goal()
    #     nav_pos.goal_pose = self.pose
    #     self.sendNavGoal(nav_pos)

    #  # dock robot
    #     self._dock_ac.wait_for_server()
    #     self.get_logger().warning('DOCKING')
    #     dock_goal = Dock.Goal()
    #     self.sendDocGoal(dock_goal)
    #     # self._dock_ac.send_goal(dock_goal)
    #     self.get_logger().warning('DOCKED')
    #     self.get_logger().warning('ALL DONE!')
    
def create():
    # rclpy.init()

    s = Slash(namespace)

    # 1 thread for the Subscription, another for the Action Clients
    exec = MultiThreadedExecutor(3)
    exec.add_node(s)

    keycom = KeyCommander([
        (KeyCode(char='n'), s.navigate),
        ])

    print("n: start random walk")
    try:
        exec.spin() # execute slash callbacks until shutdown or destroy is called
    except KeyboardInterrupt:
        print('KeyboardInterrupt, shutting down.')
        print("Shutting down executor")
        exec.shutdown()
        print("Destroying Node")
        s.destroy_node()
        print("Shutting down RCLPY")
        rclpy.try_shutdown()



if __name__ == '__main__':
    create()