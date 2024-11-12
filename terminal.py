import sys, os, shutil, random, platform
from random import randint

def echo():
    echo = input('\\terminal.py - echo input >>> $ ')
    print(f'\\terminal.py - echo >>> $ {echo}')
def plat():
    print(f'\\terminal.py - platform.platform >>> $ {platform.platform()} \n'
          f'\\terminal.py - platform.system >>> $ {platform.system()} \n'
          f'\\terminal.py - platform.release >>> $ {platform.release()}')
def diskspace():
    total, used, free = shutil.disk_usage("/")

    print("Total: %d GiB" % (total // (2**30)))
    print("Used: %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))

while True:
    terminalinput = input('\\terminal.py >>> $ ')
    if terminalinput == '.echo':
        echo()
    if terminalinput == '.platform':
        plat()
    if terminalinput == '.disk':
        diskspace()
