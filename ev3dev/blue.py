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

def blue():
    tank = MoveTank(OUTPUT_A, OUTPUT_B)
    m = MediumMotor(OUTPUT_C)
    now = ColorSensor()

    tank.on_for_rotations(50,50,0.46) # turn 90  degrees clock wise

#lineTrace()

    tank.on_for_rotations(10, 10, 0.1)

    while True:
        if now.color == 1:
            break
        else:
            m.on(50, 50)
    
    return True