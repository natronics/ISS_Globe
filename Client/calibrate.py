#!/usr/bin/env python
import gtk
import gobject
import ISS_Globe

def laser_changed(adj):
  global hardware
  hardware.move_laser(int(adj.value))
  #print "yay!!", adj.value

def globe_changed(adj):
  global hardware
  hardware.move_globe(int(adj.value))
  #print "yay!!", adj.value

def toggle_laser(btn):
  hardware.toggle_laser()
  #print btn.get_active()
  
  
""" Hardware 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

hardware = ISS_Globe.Hardware()
hardware.move_laser(90)


""" Window 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
win = gtk.Window()
win.connect("destroy", lambda x: gtk.main_quit())
win.set_default_size(800,600)
win.set_title("ISS Globe Calibrate")

vbox = gtk.VBox(False, 0)

""" Servo Control 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
control_frame = gtk.Frame("Servo Control")
control_vbox = gtk.VBox(False, 0)

""" Laser 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
laser_hbox = gtk.HBox(False, 0)

laser_label = gtk.Label("Laser: ")
laser_adj = gtk.Adjustment(value=90, lower=0, upper=181, step_incr=1, page_incr=10, page_size=1)
laser_adj.connect("value_changed", laser_changed)
laser_slider = gtk.HScale(laser_adj)
laser_slider.set_digits(0)

laser_hbox.pack_start(laser_label, False, False, 5)
laser_hbox.pack_start(laser_slider, True, True, 5)

""" Globe 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
globe_hbox = gtk.HBox(False, 0)

globe_label = gtk.Label("Globe: ")
globe_adj = gtk.Adjustment(value=90, lower=0, upper=181, step_incr=1, page_incr=10, page_size=1)
globe_adj.connect("value_changed", globe_changed)
globe_slider = gtk.HScale(globe_adj)
globe_slider.set_digits(0)

globe_hbox.pack_start(globe_label, False, False, 5)
globe_hbox.pack_start(globe_slider, True, True, 5)

""" Pack Servo 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
control_vbox.pack_start(laser_hbox, False, False, 0)
control_vbox.pack_start(globe_hbox, False, False, 0)

control_frame.add(control_vbox)

""" Laser Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
toggle_control_frame = gtk.Frame("Laser Control")
toggle_control_vbox = gtk.VBox(False, 0)
button = gtk.CheckButton("Laser On")
button.connect("toggled", toggle_laser)
toggle_control_vbox.pack_start(button, False, False, 20)
toggle_control_frame.add(toggle_control_vbox)

""" Pack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
vbox.pack_start(control_frame, False, False, 0)
vbox.pack_start(toggle_control_frame, False, False, 0)
win.add(vbox)
win.show_all()
gtk.main()

