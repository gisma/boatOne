import pantilthat
import time
import math


while True:
    # Set the maximum high pulse for a servo in microseconds.
    # pantilthat.servo_pulse_max(index, 100)
    # set position of servo one in degrees
    pantilthat.servo_one(-20)
    # set position of servo two in degrees
    pantilthat.servo_two(0)
    # get position of servo one
    #pantilthat.get_pan()

    hori = list(range(-20,20))
    vert = list(range(0,-60,-5))

    for j in vert:
        pantilthat.tilt(j)
        for i in hori:
            pantilthat.pan(i)
            time.sleep(0.01)
        
        

        

