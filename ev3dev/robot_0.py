#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_C, SpeedPercent,MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from colorChecker import colorChecker
from course import course
#TODO: Add code here
tank = MoveTank(OUTPUT_A, OUTPUT_B)
m = MediumMotor(OUTPUT_C)
now = ColorSensor(INPUT_1)
def main():
    colorChecker()

def close():
    print(close)
