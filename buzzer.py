#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) #set GPIO24 as the output for the buzze

p = GPIO.PWM(24, 1000) #set frequency to 1000Hz for better experience
p.start(0)
try:
    while 1:
       	for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
