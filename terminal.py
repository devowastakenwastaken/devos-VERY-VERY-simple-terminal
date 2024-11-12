import sys, os, shutil, random, platform
from random import randint
import tkinter as tk
from tkinter import *

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
def guiver():
    root = tk.Tk()
    root.geometry('1000x650')



    root.mainloop()
def terminal():
    while True:
        terminalinput = input('\\terminal.py >>> $ ')
        if terminalinput == '.echo':
            echo()
        if terminalinput == '.platform':
            plat()
        if terminalinput == '.disk':
            diskspace()
        if terminalinput == '.quit':
            exit()
        if terminalinput == '.gui':
            guiver()
        if terminalinput == '.?':
            pass

startup = input('start terminal? [Y/N] >>> ')
if startup == 'Y':
    terminal()
if startup == 'y':
    terminal()
if startup == 'yes':
    terminal()
if startup == 'Yes':
    terminal()
if startup == 'n':
    exit()
else:
    print('ERROR: reply to input \'startup\' - unspecified response')
    exit()




# Objectives:
# Add disk function ✔
# Add echo ✔
# Add install function
# Add YT to MP4 downloader
# Add system-intertwined commands (shutdown, install)
