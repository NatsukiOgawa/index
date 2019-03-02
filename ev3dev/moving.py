#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here

now = ColorSensor()
tank = MoveTank(OUTPUT_A, OUTPUT_B)

tank.on_for_degrees(30, 30, 30) # (A)

while True: # search "one"
    if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5:# 
        one = now.color # color number
        tank.on_for_degrees(15,15,60) # (B)
        break
    elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
        tank.on_for_degrees(15,15,45) # go ahead slight

while True: # search "two"
    if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5: # 
        two = now.color # color number
        tank.on_for_degrees(15,15,60) # (B)
        break
    elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7:  # no color or black or white
        tank.on_for_degrees(15,15,45) # go ahead slight


while True: # search "three"
    if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5: # 
        three = now.color # color number
        tank.on_for_degrees(15,15,60) # (B)
        break
    elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
        tank.on_for_degrees(15,15,45) # go ahead slight



while True: # search "four"
    if now.color == 2 or now.color == 3 or now.color == 4 or now.color == 5:# 
        four = now.color # color number
        tank.on_for_degrees(15,15,60) # (B)
        break
    elif now.color == 0 or now.color == 1 or now.color == 6 or now.color == 7: # no color or black or white
        tank.on_for_degrees(15,15,45) # go ahead slight

course = str(one) + str(two) + str(three) + str(four)

moving0(one)
moving1(two)
moving2(three)
moving3(four)




if course[0] == 4: # yellow

elif course[0] == 5: # red

elif course[0] == 2: # blue





if course[1] == 4: # yellow

elif course[1] == 5: # red

elif course[1] == 2: # blue
    
    
if course[2] == 4: # yellow

elif course[2] == 5: # red

elif course[2] == 2: # blue
    
    
    
if course[3] == 4: # yellow

elif course[3] == 5: # red

elif course[3] == 2: # blue







if course[0] == 2 or   course[1] == 2 or course[2] == 2 or course[3] == 2:
    # to go to goal1
else:
    # to go to goal2 

