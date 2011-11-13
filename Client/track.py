#!/usr/bin/env python
import gtk
import gobject
import ISS_Globe
import time

tracking = False
ISS = ISS_Globe.satellite()
hardware = ISS_Globe.Hardware()

hardware.toggle_laser()

def stop_track(btn):
  global tracking
  tracking = False
  print "stop"

def play_track(btn):
  global tracking
  tracking = True
  gobject.timeout_add_seconds(1, step_track)
  print "play"
  
def fast_track(btn):
  print "fast"

def step_track():
  if tracking:
    lat, lon = ISS.locate()
    command_pos(lat, lon)
  gobject.timeout_add_seconds(1, step_track)

def goto(btn):
  print "goto"
  lat, lon = ISS.locate()
  command_pos(lat, lon)

def map_range(out_low, out_high, range_low, range_high, val):
  a = float(out_high - out_low) / float(range_high - range_low)
  b = out_low - a * range_low
  if val < range_low:
    return out_low
  if val > range_high:
    return out_high
  return (a * val) + b

def command_pos(lat, lon):
  # Laser
  lat_servo = map_range(145, 29, -60, 60, lat)
  lat_servo = int(lat_servo)
  
  # Globe
  lon_servo = map_range(180, 0, -180, 180, lon)
  lon_servo = int(lon_servo)
  
  print lat, lon
  print lat_servo, lon_servo
  hardware.move_laser(lat_servo)
  hardware.move_globe(lon_servo)
  
def toggle_laser(btn):
    hardware.toggle_laser()
  
""" Window 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
win = gtk.Window()
win.connect("destroy", lambda x: gtk.main_quit())
win.set_default_size(200,75)
win.set_title("ISS Globe")

""" Vbox """
vbox = gtk.VBox(False, 0)

""" Time Control 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
time_frame  = gtk.Frame("Time Control")
time_hbox   = gtk.HBox(False, 0)

init_button = gtk.Button("goto")
init_button.connect("clicked", goto)
stop_button = gtk.Button("Stop")
stop_button.connect("clicked", stop_track)
play_button = gtk.Button("Real Time")
play_button.connect("clicked", play_track)
fast_button = gtk.Button("Fast!")
fast_button.connect("clicked", fast_track)
laser_button = gtk.Button("Laser")
laser_button.connect("clicked", toggle_laser)

time_hbox.pack_start(stop_button, False, False, 5)
time_hbox.pack_start(play_button, False, False, 5)
time_hbox.pack_start(fast_button, False, False, 5)
time_hbox.pack_start(init_button, False, False, 5)
time_hbox.pack_start(laser_button, False, False, 10)
time_frame.add(time_hbox)

vbox.pack_start(time_frame, False, False, 0)
win.add(vbox)

win.show_all()
gtk.main()

