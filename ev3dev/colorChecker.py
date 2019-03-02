#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_C, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from red import red
from yellow import yellow
from blue import blue
from course import course
from finish import finish

tank = MoveTank(OUTPUT_A, OUTPUT_B)
m = MediumMotor(OUTPUT_C)
now = ColorSensor(INPUT_1)

def colorChecker():
    while True: # search "one"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5:# 
            one = now.color # color number
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
            tank.on(15,15) # go ahead slight

    while True: # search "two"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5: # 
            two = now.color # color number
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7:  # no color or black or white
            tank.on(15,15) # go ahead slight

    while True: # search "three"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5: # 
            three = now.color # color number
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
            tank.on(15,15) # go ahead slight

    while True: # search "four"
        if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5:# 
            four = now.color # color number
            break
        elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
            tank.on(15,15) # go ahead slight

    tank.on_for_rotations(50,-50,0.46) # turn 90  degrees clock wise
    tank.on_for_rotations(50,50,2)
    
    while True:
        if now.color == 1:
            break
        elif  now.color != 1:
            tank.on(10, 10)

    print(one)
    print(two)
    print(three)
    print(four)

    course(one, two, three, four )    

    return (one, two,)



