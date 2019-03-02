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

# TODO: Add code here

tank = MoveTank(OUTPUT_A, OUTPUT_B)
m = MediumMotor(OUTPUT_C)
now = ColorSensor()

def lineTrace():

    base  = 45
    sousa = 0  
    hensa = 0 
    hensa_1 = 0
    kp = 0.1  
    kd = 0.1 
    d = 100

    for d in range(1,d):

        if now.reflected_light_intensity < 10:
            light = 10
        if 80 < now.reflected_light_intensity:
            light = 80
        else:
            light = now.reflected_light_intensity
   
        hensa_1 = hensa # i-2 = i-1 
        hensa = base - light # i = ~~~
        P = kp * hensa # while→p<0, black→0<p
        D = kd * (hensa - hensa_1) / d # 
        sousa =  P + D

        tank.on(sousa, sousa)

        return True
   