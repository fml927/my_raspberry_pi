import  RPi.GPIO as GPIO
import time 

'''
hardware connect: GND->PIN7, Signal->PIN8, ref "_IO_" file
'''

print('setting')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 23
GPIO.setup(led, GPIO.OUT)

print('Lopp start')
# Loop 10 times
for i in range(1, 10):
    GPIO.output(led, 1)
    time.sleep(1)
    GPIO.output(led, 0)
    time.sleep(1)

print('Loop over')
GPIO.cleanup()

print('close')
