import os
import random
import re
import serial
import datetime

os.system('amixer -q set \'Power Amplifier\' 70%')
dir = '/root/Desktop/Seinfeld'
files = os.listdir(dir)

arduino = serial.Serial('/dev/ttyUSB0', 9600)

secondsBetween = 5
minimumDistanceDeltaCm = 75
prevDistance = 0
last = datetime.datetime.utcnow() - datetime.timedelta(seconds=secondsBetween)
changed = False

while True:
    try:
        line = str(arduino.readline().strip())
    except serial.serialutil.SerialException:
        continue
    s = re.search(r'b\'(\d+)\'', line, flags=0)
    if s:
        newDistance = int(s.group(1))
        if abs(newDistance - prevDistance) > 3:
            print('previous: ' + str(prevDistance) + 'cm\t new: ' + str(newDistance) + 'cm')
            changed = True
        if (newDistance + minimumDistanceDeltaCm < prevDistance) and ((datetime.datetime.utcnow() - last).total_seconds() > secondsBetween):
            changed = True
            os.system('mplayer -ao alsa "' + dir + '/' + random.choice(files) + '"')
            last = datetime.datetime.utcnow()
        if changed:
            prevDistance = newDistance
            changed = False
