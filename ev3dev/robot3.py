#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

now = ColorSensor() #black == 8, white ==89


if now.color != 1:
    one = now.color
    tank_drive.on(10, 10, 0.5)
elif now.color == 1:
    tank_drive.on(5, 5, 0.5)








while True:

    if now.reflected_light_intensity<=10:
        now.reflected_light_intensity == 10 # 10<=black

    if 80<=now.reflected_light_intensity:
        now.reflected_light_intensity == 80 # white<=80 
        #10<=now<=80

    base  = 45# (white + black) / 2 = 45

    kp = 2

    seigyo = base - now.reflected_light_intensity #-35<=seigyo<=35
    sousa = kp * seigyo # -70<=sousa<=70 (ave == 0)
    if (-70<=sousa<-10): # on white
        print(now.reflected_light_intensity)
        sousa *= -1
        if sousa%2==0:
            tank_drive.on_for_degrees(sousa, -sousa)
        else:
            sousa += 1
            tank_drive.on_for_degrees(sousa, sousa)
    elif (10<sousa<=70): # on black
        print(now.reflected_light_intensity)
        if sousa%2==0:
            tank_drive.on(-sousa, sousa)
        else:
            sousa +=1
            tank_drive.on_for_degrees(-sousa, sousa)
    

