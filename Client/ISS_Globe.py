import serial
import time
import ephem
import math

class Hardware:
  
  device      = '/dev/ttyACM0'
  baud        = 57600
  safe_delay  = 0.001 #1ms
  
  def __init__(self):
    self.ser = serial.Serial(self.device, self.baud, timeout=0.8)

  def move_laser(self, command):
    self.ser.write('p')
    time.sleep(self.safe_delay)
    self.ser.write(chr(command))
    time.sleep(self.safe_delay)

  def move_globe(self, command):
    self.ser.write('l')
    time.sleep(self.safe_delay)
    self.ser.write(chr(command))
    time.sleep(self.safe_delay)
    
  def toggle_laser(self):
    self.ser.write('s')
    time.sleep(self.safe_delay)

  def end(self):
    self.ser.close()

class satellite:

    def __init__(self):

        # Read in ISS Data
        tle = []
        with open('data/iss.tle', 'r') as f_in:
            for i, line in enumerate(f_in):
                if i > 2: break;
                tle.append(line.strip())

        self.iss = ephem.readtle(*tle)
        self.locate()
    
    def locate(self):
        self.iss.compute()
        self.lat = math.degrees(self.iss.sublat)
        self.lon = math.degrees(self.iss.sublong)
        return self.lat, self.lon
