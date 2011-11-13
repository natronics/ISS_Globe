#!/usr/bin/env python
import serial
import math
import time

device = '/dev/ttyACM0'
ser = serial.Serial(device, 9600, timeout=0.1)

def map_range(out_low, out_high, range_low, range_high, val):
  a = float(out_high - out_low) / float(range_high - range_low)
  b = out_low - a * range_low
  if val < range_low:
    return out_low
  if val > range_high:
    return out_high
  return (a * val) + b
  
def write(lat):
  pwm = map_range(0, 180, -90, 90, lat)
  pwm = int(math.floor(pwm))
  ser.write(chr(pwm))


delay = 0.01

while (1):
  for i in range(180):
    write(i-90)
    time.sleep(delay)
    #print i -90
  for i in range(180):
    write(180 - i - 90)
    time.sleep(delay)
    #print 180 - i - 90


ser.close()
