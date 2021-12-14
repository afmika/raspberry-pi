"""
@author afmika
https://github.com/afmika
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

def turn (on = True):
    value = GPIO.HIGH if on else GPIO.LOW
    GPIO.output(18, value)
    
def infiniteLoop (n_per_sec = 10):
    state = True
    GPIO.output(18, GPIO.HIGH)
    delta = 1 / n_per_sec
    while True:
        turn (state)
        state = not state
        time.sleep(delta)

def countLoop (nax = 10):
    n = 1
    while True:
        state = False
        # on in n states
        # off in n + 1 states
        for i in range(2*n + 1):
            turn (state)
            if state:
                print ("bang")
            state = not state
            time.sleep(0.250) # ms
        print (str(n) + " DONE")
        n = n % nax
        n += 1
        time.sleep(1.)

countLoop (10)