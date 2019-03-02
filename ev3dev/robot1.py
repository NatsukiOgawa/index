#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent,MoveTank
# TODO: Add code here

m = MediumMotor(OUTPUT_A)
m.on_for_rotations(SpeedPercent(75), 5)
