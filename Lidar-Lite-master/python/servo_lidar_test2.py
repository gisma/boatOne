import RPi.GPIO as GPIO
import time
from lidar_lite import Lidar_Lite



lidar = Lidar_Lite()
connected = lidar.connect(1)
if connected < -1:
  print( "Not Connected")


servoPIN1 = 24
servoPIN2 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p1 = GPIO.PWM(servoPIN1, 50) # GPIO  als PWM mit 50Hz
p2 = GPIO.PWM(servoPIN2, 50) # GPIO  als PWM mit 50Hz

p1.start(2.5) # Initialisierung
p2.start(2.5) # Initialisierung

erg = []

# Umrechnung Grad in Tastverhaeltnis je servo
def setservo1(winkel):
  if winkel < 0:
    winkel = 0
  if winkel > 180:
    winkel = 180
  pwm = winkel/18 + 2.5
  p1.ChangeDutyCycle(pwm)

def setservo2(winkel):
  if winkel < 0:
    winkel = 0
  if winkel > 180:
    winkel = 180
  pwm = winkel/18 + 2.5
  p2.ChangeDutyCycle(pwm)

def move():
    erg = []
    lid =[]
    c = 0
    t1 = time.time()
    for i in range(58, 102, 4):
        setservo1(i)
        time.sleep(0.1)
        if c in [x for x in range(0, 50) if x%2 == 0 ]:
            for j in range(30, 95, 5):
                setservo2(j)
                time.sleep(0.1)
                dist = lidar.getDistance()
                erg.append( [i, j,dist] )
                lid.append(lidar.getDistance())
                print(i,j, dist)
            c = c+1    
        else:
            for j in range (95,30,-5):
                setservo2(j)
                time.sleep(0.1)
                dist = lidar.getDistance()
                erg.append( [i, j,dist] )
                #print(dist)
                lid.append(lidar.getDistance())
                print(i,j, dist)
            c = c+1
            
    for i in range(114, 70, -4):
        setservo1(i)
        time.sleep(0.1)
        if c in [x for x in range(0, 50) if x%2 == 0 ]:
            for j in range(30, 95, 5):
                setservo2(j)
                time.sleep(0.1)
                dist = lidar.getDistance()
                erg.append( [i, j,dist] )
                lid.append(lidar.getDistance())
                print(i,j, dist)
            c = c+1    
        else:
            for j in range (95,30,-5):
                setservo2(j)
                time.sleep(0.1)
                dist = lidar.getDistance()
                erg.append( [i, j,dist] )
                #print(dist)
                lid.append(lidar.getDistance())
                print(i,j, dist)
            c = c+1
        #print(i, j,dist)
    #GPIO.setup(servoPIN1, GPIO.OUT)
    #GPIO.setup(servoPIN2, GPIO.OUT)
    #p1 = GPIO.PWM(servoPIN1, 50) # GPIO  als PWM mit 50Hz
    #p2 = GPIO.PWM(servoPIN2, 50) # GPIO  als PWM mit 50Hz
    #p1.start(2.5) # Initialisierung
    #p2.start(2.5) # Initialisierung
    
    print(i,j, dist)
    #print(c)
    #t2 =time.time()
    #print(t2-t1)
    #print(erg)
    return(erg)

try:
  # Endlosschleife Servoansteuerung
  while True:
      t1 = time.time()
      test = move()
      t2 = time.time()
      print(t2-t1)
except KeyboardInterrupt:
  # Abbruch mit [Strg][C],
  GPIO.cleanup()

