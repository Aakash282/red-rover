import RPi.GPIO as gpio
import time
import sys
from sensor import distance
import random

class Rover:
  def __init__(self):
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

  def forward(self, tf):
    gpio.output(7,  False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

  def reverse(self, tf):
    gpio.output(7,  True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

  def turn_left(self, tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

  def turn_right(self, tf):
    gpio.output(7, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.cleanup()

  def pivot_left(self, tf):
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(tf)
    gpio.cleanup()
    

  def pivot_right(self, tf):
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, False)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.cleanup()


def check_up():
  dist = distance()

  if dist < 25:
    print('Too close,',dist)
    init()
    reverse(2)
    dist = distance()
    if dist < 25:
      print('Too close,',dist)
      init()
      pivot_left(3)
      init()
      reverse(2)
      dist = distance()
      if dist < 25:
        print('Too close, giving up', dist)
        sys.exit()

def autonomy():
  tf = 0.030
  x = random.randrange(0,4)

  if x == 0:
    for y in range(30):
      check_front()
      init()
      forward(self, tf)
  elif x == 1:
    for y in range(30):
      check_front()
      init()
      pivot_left(self, tf)
  elif x == 2:
    for y in range(30):
      check_front()
      init()
      turn_right(self, tf)
  elif x == 3:
    for y in range(30):
      check_front()
      init()
      turn_left(self, tf)

