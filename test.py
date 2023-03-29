# for mycobot,mecharm
from pymycobot.mycobot import MyCobot

# for mypalletizer
from pymycobot.mypalletizer import MyPalletizer

# for myBuddy
from pymycobot.mybuddy import MyBuddy

mycobot = MyCobot()
mycobot.send_angles([0,0,0,0,0,0], 80)
