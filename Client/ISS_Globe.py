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

    self.iss = ephem.readtle("ISS",             
        "1 25544U 98067A   11317.43923700  .00025400  00000-0  30934-3 0  4247"
      , "2 25544  51.6402 129.5626 0021849  53.2994  33.8338 15.60068263744210")

    self.locate()
    
  def locate(self):
    self.iss.compute()
    self.lat = math.degrees(self.iss.sublat)
    self.lon = math.degrees(self.iss.sublong)
    return self.lat, self.lon
