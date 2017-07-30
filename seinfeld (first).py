import os
import random
import time
import sys
import CHIP_IO.GPIO as GPIO

os.system('amixer -q set \'Power Amplifier\' 20%')
files = os.listdir('Seinfeld')

pingPin = "XIO-P7"
duration = 1000
alpha = 0
beta = 0
gamma = 0
delta = 0

try:
    while True:
        GPIO.cleanup()
        GPIO.setup(pingPin, GPIO.OUT)
        #GPIO.output(pingPin, GPIO.LOW)
        #time.sleep(2.0/1000000.0)
        GPIO.output(pingPin, GPIO.HIGH)
        time.sleep(0.00075)
        #time.sleep(5.0/1000000.0)
        #GPIO.output(pingPin, GPIO.LOW)
        
        #GPIO.cleanup()
        GPIO.setup(pingPin, GPIO.IN)
        GPIO.input(pingPin)
        
        while GPIO.input(pingPin) == 1 and delta < 20:
            delta = delta + 1
        else:
            beta = time.time()
            gamma = beta - alpha
            print(str(gamma))
            #sys.stdout.write(str(gamma))
            #sys.stdout.flush()

        #duration = GPIO.input(pingPin)
        #print(duration)
        #sys.stdout.write(str(duration))
        #sys.stdout.flush()
        time.sleep(500.0/1000.0)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

#os.system('mplayer -ao alsa Seinfeld/' + files[random.randint(0, len(files))])