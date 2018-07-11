import pantilthat
import time
import math

# Set the maximum high pulse for a servo in microseconds.
# pantilthat.servo_pulse_max(index, 100)
# set position of servo one in degrees
pantilthat.servo_one(-90)
# set position of servo two in degrees
pantilthat.servo_two(-10)
# get position of servo one
pantilthat.get_pan()

# ----- 
a = 0
stop = 0
while True:
    # Get the time in seconds
    t = time.time()

    # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
    a = math.sin(t * 2) * 90
    
    # Cast a to int for v0.0.2
    a = int(a)

    pantilthat.pan(a)
    pantilthat.tilt(0)

    # Two decimal places is quite enough!
    print(a, t)

    # Sleep for a bit so we're not hammering the HAT with updates
    time.sleep(0.005)
    if pantilthat.get_pan() == 89:
        break
   