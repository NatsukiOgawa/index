#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from course import course
from robot_0 import close
# TODO: Add code here


def finish():
    tank = MoveTank(OUTPUT_A, OUTPUT_B)
    m = MediumMotor(OUTPUT_C)
    now = ColorSensor()

    if goal == 1:
        tank.on_for_rotations(50, -50, 0.46)
        # lineTrace
        # go to goal1
        return True

    elif goal == 2:
        tank.on_for_rotations(-50, 50, 0.46)
        # lineTrace
        # go to goal2
        return True

    close = "FINISH!!"

    close(close)