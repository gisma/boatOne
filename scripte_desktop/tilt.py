import pantilthat
import math
import time

# Set the maximum high pulse for a servo in microseconds.
# pantilthat.servo_pulse_max(index, 100)
# set position of servo one in degrees
pantilthat.servo_one(90)
# set position of servo two in degrees
pantilthat.servo_two(-10)
# get position of servo one
pantilthat.get_pan()
# class pantilthat.PanTilt(enable_lights=True, idle_timeout=2, light_mode=1, light_type=0, servo1_min=575, servo1_max=2325, servo2_min=575, servo2_max=2325, address=21, i2c_bus=None)

# --------

#!/usr/bin/env python

l = [0,5,10,15,20,25,30,35,40,45,50,55,60]

 #   for i in range(len(l)):
 #   pantilthat.tilt(i)
    
    # ----
lo=0
for i in range(len(l)):
     while (True):
          pantilthat.tilt(lo)
          lo+=5
     if lo+l[i]>115:
         break
     print(lo)    
    
    
    
    
#        while True:
    # Get the time in seconds
#        t = time.time()
    # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
 #   a = math.sin(t * 2) * 15
    
    # Cast a to int for v0.0.2
  #  a = int(a)

   # pantilthat.pan(a)

    # Two decimal places is quite enough!
    #print(round(a,2),i, t)
    

        

    # 5 grad for each loop

    # Sleep for a bit so we're not hammering the HAT with updates
time.sleep(0.005)
    
 