import RPi.GPIO as gpio
import time
import sys
from lib.Rover import Rover
from lib.sensor import distance
import random

for z in range(10):
    autonomy()