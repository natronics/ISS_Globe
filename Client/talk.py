#!/usr/bin/env python
import serial
import time

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0.1)

for i in range(256):
  ser.write(chr(i))
  time.sleep(0.01)

ser.close()
