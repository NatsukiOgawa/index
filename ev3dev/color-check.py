#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
now = ColorSensor() # black == 8 and while == 89




while True:
    if now.color != 1: # not black
        one = now.color 
        tank_drive.on_for_seconds(SpeedPercent(5), SpeedPercent(5), 1)
        break # black
    elif now.color == 1: 
        tank_drive.on_for_seconds(SpeedPercent(5), SpeedPercent(5), 1)

        
        print("red")
    elif now.color == 6:
        print("white")
    elif now.color == 7:
        print("brown")