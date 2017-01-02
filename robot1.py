import RPi.GPIO as gpio
import time

print 1

gpio.setmode(gpio.BOARD)

# gpio.setup(7,gpio.OUT)
# gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
# gpio.setup(15,gpio.OUT)

print 2
# def forward_RIGHT():
# 	gpio.output(7,True)
# 	gpio.output(11,False)
# def backward_RIGHT():
# gpio.output(13,False)
# gpio.output(15,True)

gpio.output(13, True)
# gpio.output(15, True)

time.sleep(0.5)
print 3
gpio.cleanup()

