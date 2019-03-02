#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_２
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here

course = ""
now = ColorSensor()


if now.color!=1: # not black

    if now.color==2: # blue

        course += "B"
        # two objects
    
    elif now.color == 4: # yellow
        course += "Y"
        # wall on "1" and object on "2"

    elif now.color == 5: # red
        course += "R"
        # wall on "2" and object on "1"

    elif now.color == 6: # white
        course += "w"
        #do something 

print(course)

