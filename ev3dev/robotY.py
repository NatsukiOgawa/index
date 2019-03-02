#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)


tank_drive.on_for_rotations(50,-50,0.5) # 90 degrees turn clock wise

tank_drive.on_for_rotations(-50,50,0.5) # 90 degrees turn opporsite






