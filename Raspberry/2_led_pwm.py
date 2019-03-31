import  RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

Led = 23
gpio.setup(Led, gpio.OUT)

print('setting: freq=0.5, dc=50 (0-100)')
p= gpio.PWM( Led, 0.5)
p.start(50)
input("return for STOP ...")

print('setting: freq=1, dc=50 (0-100)')
p.ChangeFrequency(1)
input("return for STOP ...")

print('setting: freq=2, dc=50 (0-100)')
p.ChangeFrequency(2)
input("return for STOP ...")

print('setting: freq=2, dc=10 (0-100)')
p.ChangeDutyCycle(10)
input("return for STOP ...")


print('setting: freq=10, dc=50 (0-100)')
p.ChangeFrequency(10)
p.ChangeDutyCycle(50)
input("return for STOP ...")

print('setting: freq=100, dc=50 (0-100)')
p.ChangeFrequency(100)
input("return for STOP ...")


p.stop()
gpio.cleanup()