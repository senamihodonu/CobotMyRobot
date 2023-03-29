# for mycobot,mecharm
from pymycobot.mycobot import MyCobot

# for mypalletizer
from pymycobot.mypalletizer import MyPalletizer

# for myBuddy
from pymycobot.mybuddy import MyBuddy

coords = mc.get_coords()
print(coords)
mycobot = MyCobot("/dev/ttyAMA0", 115200)
mycobot.send_angles([0,0,0,0,0,0], 80)
mycobot.send_coords([160, 160, 160, 0, 0, 0], 70, 0)
