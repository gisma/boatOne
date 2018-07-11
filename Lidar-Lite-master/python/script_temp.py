#!/usr/bin/python
# -*- coding: utf-8 -*-

#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN)
def temp_messen():
    # 1-Wire Slave-Liste lesen
    file = open('/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves')
    w1_slaves = file.readlines()
    file.close()

    # Fuer jeden 1-Wire Slave aktuelle Temperatur ausgeben
    for line in w1_slaves:
      # 1-wire Slave extrahieren
      w1_slave = line.split("\n")[0]
      # 1-wire Slave Datei lesen
      file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
      filecontent = file.read()
      file.close()

      # Temperaturwerte auslesen und konvertieren
      stringvalue = filecontent.split("\n")[1].split(" ")[9]
      temperature = float(stringvalue[2:]) / 1000

      # Temperatur ausgeben
      print(str(w1_slave) + ': %6.2f °C' % temperature)
    return(temperature)

temp_messen()