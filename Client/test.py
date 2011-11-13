#!/usr/bin/env python
import ISS_Globe
import time

hardware = ISS_Globe.Hardware()

hardware.toggle_laser()

hardware.move_laser(90)
for i in range(90,180):
  hardware.move_laser(i)
  time.sleep(0.02)
hardware.move_laser(0)

hardware.end()
