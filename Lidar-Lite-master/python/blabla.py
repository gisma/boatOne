import RPi.GPIO as GPIO
import time
from lidar_lite import Lidar_Lite
GPIO.cleanup()


lidar = Lidar_Lite()
connected = lidar.connect(1)
if connected < -1:
  print( "Not Connected")


servoPIN1 = 18
servoPIN2 = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p1 = GPIO.PWM(servoPIN1, 50) # GPIO  als PWM mit 50Hz
p2 = GPIO.PWM(servoPIN2, 50) # GPIO  als PWM mit 50Hz

p1.start(5) # Initialisierung
p2.start(8) # Initialisierung

GPIO.cleanup()