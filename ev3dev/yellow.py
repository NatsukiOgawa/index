#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from lineTrace import lineTrace

# TODO: Add code here

def yellow():
    tank = MoveTank(OUTPUT_A, OUTPUT_B)
    m = MediumMotor(OUTPUT_C)
    now = ColorSensor()

    tank.on_for_rotations(-50,50,0.46) # turn 90  degrees clock wise

#####linetrace


    while True:
        if now.color == 5: # red tape
            m.on_for_rotations(-20,0.2)
            break
        else:
            tank.on(15, 15)
        
    tank.on_for_rotations(50,-50,0.93) # turn 180  degrees clock wise


    # lineTrace

    while True:
        if now.color == 5:
            m.on_for_rotations(SpeedPercent(5),0.2)
            break
        else:
            tank.on(15, 15)

    tank.on_for_rotations(-15, 15, 1)

    tank.on_for_rotations(50,-50,0.93) # turn 90  degrees clock wise

    tank.on_for_rotations(50, 50, 2)

    tank.on_for_rotations(30,-30,0.46)

    return True