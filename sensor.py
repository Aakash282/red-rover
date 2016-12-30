import RPi.GPIO as gpio
import time
import sys

def distance(measure='cm'):
    try:
        print 'setting up'
        gpio.setmode(gpio.BOARD)
        print 'set board'
        gpio.setup(12, gpio.OUT)
        print 'set pin 12'
        gpio.setup(16, gpio.IN)
#        gpio.setwarnings(False)
        print 'set pin 16'
        print 'computing distance'
        gpio.output(12, False)
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()

        tl = sig - nosig

        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        # gpio.cleanup()
        return distance
    except:
        e = sys.exc_info()[0]
        print e
        print 'exception'
        distance = 100
        # gpio.cleanup()
        return distance
    finally:
        print 'finished - cleaning up'
        gpio.cleanup()
		
if __name__ == "__main__":
    print(distance('cm'))
    # gpio.cleanup()
