#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from red import red
from blue import blue
from yellow import yellow
from finish import finish
# TODO: Add code here
tank = MoveTank(OUTPUT_A, OUTPUT_B)
m = MediumMotor(OUTPUT_C)
now = ColorSensor()

def course(one, two, three, four):
    if one == 4: # yellow
        yellow()
    elif one == 5: # red
        red()
    elif one == 2: # blue
        blue()

    print("one one")


    
    if two == 4: # yellow
        yellow()
    elif two == 5: # red
        red()
    elif two == 2: # blue
        blue()
    
    print("two two")

    if three == 4: # yellow
        yellow()
    elif three == 5: # red
        red()
    elif three == 2: # blue
        blue()
   
    print("three three")

    if four == 4: # yellow
        yellow()
    elif four == 5: # red
        red()
    elif four == 2: # blue
        blue()

    print("four four")




    if one != 2 or two != 2 or three != 2 or four != 2:
        goal = 2
    else:
        goal = 1

    finish(goal)
