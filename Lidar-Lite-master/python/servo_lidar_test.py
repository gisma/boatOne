import RPi.GPIO as GPIO
import time
from lidar_lite import Lidar_Lite
GPIO.cleanup()




lidar = Lidar_Lite()
connected = lidar.connect(1)
if connected < -1:
  print( "Not Connected")




servoPIN1 = 23
servoPIN2 = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p1 = GPIO.PWM(servoPIN1, 50) # GPIO  als PWM mit 50Hz
p2 = GPIO.PWM(servoPIN2, 50) # GPIO  als PWM mit 50Hz


p1.start(0) # Initialisierung
p2.start(0) # Initialisierung

erg = []

def move():
    erg = []
    lid =[]
    c = 0 
    #t1 = time.time()
    for i in range(45, 75, 5):
        for j in range (45,105,3):
            p1.ChangeDutyCycle(j/10)
            p2.ChangeDutyCycle(i/10)
            time.sleep(0.01)
            #print(lidar.getDistance())
            #print(lidar.getVelocity())
            #print(i,j)
            dist = lidar.getDistance()
            erg.append( [j, i,dist] )
            print(dist)
            lid.append(lidar.getDistance())
            c = c+1
            
    #t2 =time.time()
    #print(t2-t1)
    return(lid)


test = move()
#move()

print(test)

GPIO.cleanup()
