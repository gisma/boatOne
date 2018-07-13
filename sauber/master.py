import RPi.GPIO as GPIO
import servo_lidar_test2 as sl
from lidar_lite import Lidar_Lite

import script_temp as st

import time
import datetime




# setup
#ich bin mir unsicher ob beim importieren die ganzen Variablen mitimportiert werden oder nicht
lidar = Lidar_Lite()
connected = lidar.connect(1)
if connected < -1:
  print( "Not Connected")


pin_temp = 4
#18 , 23 oder 24
servoPIN1 = 18
servoPIN2 = 23


GPIO.setmode(GPIO.BCM)

GPIO.setup(pin_temp, GPIO.IN)


GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p1 = GPIO.PWM(servoPIN1, 50) # GPIO  als PWM mit 50Hz
p2 = GPIO.PWM(servoPIN2, 50) # GPIO  als PWM mit 50Hz

p1.start(2.5) # Initialisierung
p2.start(2.5) # Initialisierung

lid_data = []
temp_data = []

while True:
    #vielleicht auch mehr Zyklen
    for i in range(10):
        lid_data.append(sl.move())
        temp_data.append( [chr(datetime.datetime.now()), st.temp_messen()] )
    #FEEDBACK LED AN
    save_lid = open("PFAD/ZUR/DATEI/lidar_data.txt", "a")
    save_lid.write(lid_data)
    save_lid.close()
    save_temp = open("PFAD/ZUR/DATEI/temp_data.txt", "a")
    save_temp.write(temp_data)
    save_temp.close()
    #FEEDBACK LED AUS
    #NUR ABSCHALTEN WENN LED NICHT LEUCHTET oder FARBCODE gruen rot
