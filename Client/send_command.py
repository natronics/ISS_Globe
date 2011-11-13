#!/usr/bin/env python
import serial
import sys

device = '/dev/ttyACM1'
ser = serial.Serial(device, 57600, timeout=0.8)

pwm = sys.argv[1]
pwm = int(pwm)

ser.write(chr(pwm))
#print str(pwm)

ser.close()
