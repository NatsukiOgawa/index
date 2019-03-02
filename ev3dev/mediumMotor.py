#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
m = MediumMotor(OUTPUT_C)

while True:        
    m.on_for_rotations(SpeedPercent(5),0.2)

