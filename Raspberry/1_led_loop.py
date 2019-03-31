from os import *
from time import *

"""
# usage:
# 1. into terminal 'sudo su' switch to ROOT
# 2. exec this file by "python led_loop.py"
"""

while True:
    system('echo 1 >  /sys/class/leds/led0/brightness')
    sleep(1)
    system('echo 0 >  /sys/class/leds/led0/brightness')
    sleep(1)
    