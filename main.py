#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2023  <live-chst@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import RPi.GPIO as GPIO
import time
from PIL import Image
f = open('data.txt', 'r')

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def Buzz(pitch, duraction):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duraction * pitch)
    for i in range(cycles):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(17, GPIO.LOW)
        time.sleep(delay)
i = 1
j = 1
k = 1
l = 1
count = 0

for line in f:
    count = count + 1
    print(line)
    if (count == 1):
        image = Image.open('1.jpg')
    if (count == 2):
        image = Image.open('2.jpg')
    if (count == 3):
        image = Image.open('3.jpg')
    if (count == 4):
        image = Image.open('4.jpg')
    if (count == 5):
        image = Image.open('5.jpg')
    if (count == 6):
        image = Image.open('6.jpg')
    image.show()
    while(j == 1):
        if (GPIO.input(27) == 0 and k  != 2):
            #print("hap")
            k = 2
            #GPIO.output(17, GPIO.HIGH)
            #time.sleep(0.5)
            Buzz(3000, 0.1)
            #GPIO.output(17, GPIO.LOW)
        if (k == 2 and GPIO.input(27) == 1):
            #print("hop")
            j = 2
    j = 1
    k = 1
    image.close()
    if (line[0] == '1'):
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
    if (line[0] == '2'):
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
    if (line[0] == '3'):
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
    if (line[0] == '4'):
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
    time.sleep(1)
time.sleep(3)
f.close()
GPIO.cleanup()
def main(args):
    print("sup")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
