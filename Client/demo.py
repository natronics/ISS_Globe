#!/usr/bin/env python
import ISS_Globe
import math
import sys

def map_range(out_low, out_high, range_low, range_high, val):
  a = float(out_high - out_low) / float(range_high - range_low)
  b = out_low - a * range_low
  if val < range_low:
    return out_low
  if val > range_high:
    return out_high
  return (a * val) + b
  
hardware = ISS_Globe.Hardware()

if sys.argv[1] == 'l': 
  hardware.toggle_laser()
  exit()

lat = float(sys.argv[1])
lon = float(sys.argv[2])

# Laser
lat_servo = map_range(145, 29, -60, 60, lat)
lat_servo = int(round(lat_servo))

# Globe
lon_servo = map_range(180, 0, -180, 180, lon)
lon_servo = int(round(lon_servo))

print lat, lon
print lat_servo, lon_servo
hardware.move_laser(lat_servo)
hardware.move_globe(lon_servo)
