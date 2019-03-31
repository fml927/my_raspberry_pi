import  RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 23
GPIO.setup(led, GPIO.OUT)

# Loop 10 times
for i in range(1, 10):
    GPIO.output(led, 1)
    time.sleep(1)
    GPIO.output(led, 0)
    time.sleep(1)

GPIO.cleanup()