#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_C, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from red import red
from yellow import yellow
from blue import blue

tank = MoveTank(OUTPUT_A, OUTPUT_B)
m = MediumMotor(OUTPUT_C)
now = ColorSensor(INPUT_2)

def colorChecker():
    while True: # search "one"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5:# 
            one = now.color # color number
            tank.on_for_degrees(15,15,100) # (B)
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
            tank.on_for_degrees(15,15,45) # go ahead slight

    while True: # search "two"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5: # 
            two = now.color # color number
            tank.on_for_degrees(15,15,60) # (B)
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7:  # no color or black or white
            tank.on_for_degrees(15,15,45) # go ahead slight

    while True: # search "three"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5: # 
            three = now.color # color number
            tank.on_for_degrees(15,15,60) # (B)
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
            tank.on_for_degrees(15,15,45) # go ahead slight

    while True: # search "four"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5:# 
            four = now.color # color number
            tank.on_for_degrees(15,15,60) # (B)
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
            tank.on_for_degrees(15,15,45) # go ahead slight

    tank.on_for_rotations(10,-10,0.46) # turn 90  degrees clock wise
    tank.on_for_rotations(50,50,2)
    

    

    



