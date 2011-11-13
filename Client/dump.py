#!/usr/bin/env python
import serial

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0.1)

while(1):
  line = ser.readline()
  print line
ser.close()
