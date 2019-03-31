import  RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)

p= gpio.PWM( 12, 0.5)
p.start(1)
input("return for STOP ...")

p.stop()
gpio.cleanup()