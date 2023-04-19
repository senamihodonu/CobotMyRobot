import random
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.qos import qos_profile_sensor_data
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from geometry_msgs.msg import PoseStamped
from action_msgs.msg._goal_status import GoalStatus

import irobot_create_msgs
from irobot_create_msgs.action import DriveDistance, Undock, Dock, NavigateToPosition, RotateAngle
from irobot_create_msgs.msg import HazardDetectionVector
from irobot_create_msgs.srv import ResetPose

from pynput.keyboard import KeyCode
from key_commander import KeyCommander
from threading import Lock
from rclpy.executors import MultiThreadedExecutor


# To help with Multithreading
lock = Lock()

class Roomba(Node):
    """
    Class to coordinate actions and subscriptions
    """

    def __init__(self, namespace):
        super().__init__('slasher')

        # 2 Seperate Callback Groups for handling the bumper Subscription and Action Clients
        cb_Subscripion = MutuallyExclusiveCallbackGroup()
        #cb_Action = cb_Subscripion
        cb_Action =MutuallyExclusiveCallbackGroup()
        cb_srv =MutuallyExclusiveCallbackGroup()

        # Subscription to Hazards, the callback function attached only looks for bumper hits
        self.subscription = self.create_subscription(
            HazardDetectionVector, f'/{namespace}/hazard_detection', self.listener_callback, qos_profile_sensor_data,callback_group=cb_Subscripion)

        # Action clients for movements
        self._undock_ac = ActionClient(self, Undock, f'/{namespace}/undock',callback_group=cb_Action)
        self._drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance',callback_group=cb_Action)
        self._rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle',callback_group=cb_Action)
        self._dock_ac = ActionClient(self, Dock, f'/{namespace}/dock',callback_group=cb_Action)
        self._pos_ac = ActionClient(self, NavigateToPosition, f'/{namespace}/navigate_to_position',callback_group=cb_Action)

        # Variables
        self._goal_uuid = None

        self.reset = self.create_client(ResetPose, f'/{namespace}/reset_pose',callback_group=cb_srv)
        self.req = ResetPose.Request()



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

                    self.get_logger().warning('BACKUP')
                    canceled_drive = DriveDistance.Goal()
                    canceled_drive.distance = -0.1
                    drive_handle = self._drive_ac.send_goal_async(canceled_drive)
                    while not drive_handle.done():
                        pass # Wait for Action Server to accept goal
            
                    self.get_logger().warning('DRIVE ACCEPTED')
                    # Hold ID in case we need to cancel it
                    self._goal_uuid = drive_handle.result() 

                while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
                    pass # Wait until a Status has been assigned

                # After getting goalID, Loop while the goal is currently running
                while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
                    pass


#--------------------Async send goal calls-----------------------------
    def sendDriveGoal(self,goal):
        """
        Sends a drive goal asynchronously and 'blocks' until the goal is complete
        """

        canceled = False
        
        with lock:
            self.get_logger().warning('DRIVE LOCK')
            drive_handle = self._drive_ac.send_goal_async(goal)
            while not drive_handle.done():
                pass # Wait for Action Server to accept goal
            
            self.get_logger().warning('DRIVE ACCEPTED')
            # Hold ID in case we need to cancel it
            self._goal_uuid = drive_handle.result() 

        while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
            pass # Wait until a Status has been assigned

        # After getting goalID, Loop while the goal is currently running
        while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
            if self._goal_uuid.status is GoalStatus.STATUS_CANCELED:
                canceled = True
                break # If the goal was canceled, stop looping otherwise loop till finished
            pass
        
        with lock:
            # Reset the goal ID, nothing should be running
            self._goal_uuid = None 
        return canceled

#----------------------------------------------------------------------
    def sendTurnGoal(self,goal):
        """
        Sends a drive goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            drive_handle = self._rotate_ac.send_goal_async(goal)
            while not drive_handle.done():
                pass # Wait for Action Server to accept goal
            
            # Hold ID in case we need to cancel it
            self._goal_uuid = drive_handle.result() 

        while self._goal_uuid.status == GoalStatus.STATUS_UNKNOWN:
            pass # Wait until a Status has been assigned

        # After getting goalID, Loop while the goal is currently running
        while self._goal_uuid.status is not GoalStatus.STATUS_SUCCEEDED:
            if self._goal_uuid.status is GoalStatus.STATUS_CANCELED:
                break # If the goal was canceled, stop looping otherwise loop till finished
            pass
        
        with lock:
            # Reset the goal ID, nothing should be running
            self._goal_uuid = None 

#----------------------------------------------------------------------
    def sendDockGoal(self):
        """
        Sends a drive goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            self._dock_ac.wait_for_server()
            dock_goal = Dock.Goal()
            self._dock_ac.send_goal(dock_goal)

#----------------------------------------------------------------------
    def sendNavigateGoal(self,goal):
        """
        Sends a drive goal asynchronously and 'blocks' until the goal is complete
        """
        
        with lock:
            self._pos_ac.wait_for_server()
            self._pos_ac.send_goal(goal)

#----------------------------------------------------------------------
    def unDock(self):
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
        self.reset.call(self.req)

        return(True)

#----------------------------------------------------------------------
    def drive(self, distance):
    # wait for DriveDistance action server (blocking)
        self._drive_ac.wait_for_server()
        self.get_logger().warning('SETTING')
        
    # create goal object and specify distance to drive
        drive_goal = DriveDistance.Goal()
        drive_goal.distance = distance
        #self._drive_ac.send_goal(drive_goal)
        self.sendDriveGoal(drive_goal)

        return(True)

#----------------------------------------------------------------------
    def turn(self, degrees):
        self._rotate_ac.wait_for_server()
        self.get_logger().warning('TURNING')
        turn_goal = RotateAngle.Goal()
        turn_goal.angle = (float(degrees) * (3.14/float(180)))
        self.sendTurnGoal(turn_goal)

        return(True)

#----------------------------------------------------------------------
    def toPosition(self, position):
        self._pos_ac.wait_for_server()
        self.get_logger().warning('HEADING BACK')
        #self.position.pose.position.x -= 0.5

        pos_goal = NavigateToPosition.Goal()
        pos_goal.goal_pose = position
        self.get_logger().warning('SENDING BACK')
        self.sendNavigateGoal(pos_goal)

        return(True)

#----------------------------------------------------------------------
    def dock(self):
        self.sendDockGoal()

#----------------------------------------------------------------------
    def getPosition(self):
        print(PoseStamped())

        return PoseStamped()

#----------------------------------------------------------------------
    def drive_away(self):
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

    # wait for DriveDistance action server (blocking)
        self._drive_ac.wait_for_server()
        self.get_logger().warning('SETTING')
        
    # create goal object and specify distance to drive
        drive_goal = DriveDistance.Goal()
        drive_goal.distance = 1.0
        #self._drive_ac.send_goal(drive_goal)
        self.sendDriveGoal(drive_goal)

    # send goal to async function
        for i in range(2):
            self._rotate_ac.wait_for_server()
            if i == 0:
                self.reset.call(self.req)
                self.position = PoseStamped()
                print(self.position)
            self.get_logger().warning('TURNING')
            turn_goal = RotateAngle.Goal()
            turn_goal.angle = (float((random.randrange(0,360))) * (3.14/float(180)))

            self.sendTurnGoal(turn_goal)

            self._drive_ac.wait_for_server()
            self.get_logger().warning('DRIVING')
            drive_goal = DriveDistance.Goal()
            drive_goal.distance = 0.75

            canceled = self.sendDriveGoal(drive_goal)
            if canceled == True:
                    canceled_turn = RotateAngle.Goal()
                    canceled_turn.angle = 3.14159
                    self._rotate_ac.wait_for_server()
                    self.get_logger().warning('CANCELED TURN')
                    self.sendTurnGoal(canceled_turn)
                    self.get_logger().warning('CANCELED DRIVE')
                    self._drive_ac.wait_for_server()
                    canceled_drive = DriveDistance.Goal()
                    canceled_drive.distance = 0.5
                    self.sendDriveGoal(canceled_drive)

    # go back to dock
        self._pos_ac.wait_for_server()
        self.get_logger().warning('HEADING BACK')
        self.position.pose.position.x -= 0.5

        pos_goal = NavigateToPosition.Goal()
        pos_goal.goal_pose = self.position

        self.get_logger().warning('SENDING BACK')
        self.sendNavigateGoal(pos_goal)
        self.sendDockGoal()





if __name__ == '__main__':
    rclpy.init()

    namespace = 'create3_0585'
    s = Roomba(namespace)

    # 1 thread for the Subscription, another for the Action Clients
    exec = MultiThreadedExecutor(2)
    exec.add_node(s)

    keycom = KeyCommander([
        (KeyCode(char='r'), s.drive_away),
        ])

    print("r: Start drive_away")
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
