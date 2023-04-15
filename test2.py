# for mycobot,mecharm
from pymycobot.mycobot import MyCobot

# for mypalletizer
from pymycobot.mypalletizer import MyPalletizer

# for myBuddy
from pymycobot.mybuddy import MyBuddy


mycobot = MyCobot("/dev/ttyAMA0", 115200)
coords = mycobot.get_coords()
print(coords)
mycobot.send_angles([0,0,0,0,0,0], 80)
mycobot.seset_gripper_state(1, 50)
# mycobot.send_coords([160, 160, 160, 0, 0, 0], 70, 0)
