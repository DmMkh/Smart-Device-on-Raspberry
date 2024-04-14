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

i = 1

for line in f:
    print(line)
    if (line[0] == '1'):
        GPIO.output(24, GPIO.HIGH)
    else:
        GPIO.output(24, GPIO.LOW)
    time.sleep(0.5)

f.close()
GPIO.cleanup()
def main(args):
    print("sup")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
